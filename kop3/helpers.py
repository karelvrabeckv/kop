# Module helpers

"""
Load instances.
"""
def get_instances(path):
  lines = []
  with open(path) as f:
    lines = f.readlines()

  instances = []
  for line in lines:
    data = line.split()

    weights, costs = [], []
    for i in range(3, len(data), 2):
      weights.append(int(data[i]))
      costs.append(int(data[i + 1]))

    instance = {
      "ID": int(data[0]),
      "n": int(data[1]),
      "M": int(data[2]),
      "w": weights,
      "c": costs,
    }
    instances.append(instance)
  return instances

"""
Get the total time including
the average and maximum time.
"""
def get_time_data(results):
  time_of_set = avg_time = max_time = 0
  for result in results:
    # Solve the total time
    time_of_set += result[1]

    # Solve the maximum time
    if result[1] > max_time:
      max_time = result[1]
  
  # Solve the average time
  avg_time = time_of_set / len(results)

  return (format(time_of_set, ".5f"), format(avg_time, ".5f"), format(max_time, ".5f"))

"""
Get the total errors including
the average and maximum error.
"""
def get_error_data(results):
  errors_of_set = avg_error = max_error = 0
  for result in results:
    # Solve the total errors
    if result[2]:
      errors_of_set += 1

    # Solve the maximum error
    if result[2] > max_error:
      max_error = result[2]

    # Solve the average error
    avg_error += result[2]
  avg_error /= len(results)

  return (errors_of_set, format(avg_error, ".5f"), format(max_error, ".5f"))
