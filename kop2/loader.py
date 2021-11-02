# Module loader

import constants as c

"""
Load instances.
"""
def get_instances(path):
  lines = []
  with open(path + c.INST_FILE_POSTFIX) as f:
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
Load solutions.
"""
def get_solutions(path):
  lines = []
  with open(path + c.SOL_FILE_POSTFIX) as f:
    lines = f.readlines()

  last_id, solutions = 'x', []
  for line in lines:
    data = line.split()

    solution = {
      "ID": int(data[0]),
      "n": int(data[1]),
      "C": int(data[2]),
      "t": list(map(int, data[3:])),
    }

    if last_id != 'x' and last_id == solution["ID"]:
      continue
    
    last_id = solution["ID"]
    solutions.append(solution)
  return solutions
