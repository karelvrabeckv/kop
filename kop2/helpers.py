# Module helpers

"""
Get the total time including
the average and maximum time.
"""
def getTimeData(results):
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
def getErrorData(results):
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
