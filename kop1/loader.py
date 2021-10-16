# Module loader

# Load instances
def get_instances(path):
  lines = []
  with open(path) as f:
    lines = f.readlines()

  instances = []
  for line in lines:
    data = line.split()

    weights = []
    costs = []
    for i in range(4, len(data), 2):
      weights.append(int(data[i]))
      costs.append(int(data[i + 1]))

    instance = {
      "numOfThings": int(data[1]),
      "maxWeight": int(data[2]),
      "minCost": int(data[3]),
      "weights": weights,
      "costs": costs,
    }
    instances.append(instance)
  return instances

# Load solutions
def get_solutions(path):
  lines = []
  with open(path) as f:
    lines = f.readlines()

  solutions = []
  for line in lines:
    data = line.split()
    solution = {
      "totalCost": int(data[2]),
      "occurrences": list(map(int, data[3:])),
    }
    solutions.append(solution)
  return solutions
