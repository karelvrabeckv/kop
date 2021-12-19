# Module loader

import numpy as np

"""
Load instances.
"""
def get_instances(path):
  with open(path) as f:
    lines = f.readlines()

  instances = []
  for line in lines:
    data = line.split()

    instance = {
      "n": int(data[1]),
      "M": int(data[2]),
      "w": np.array([int(data[i]) for i in range(3, len(data), 2)]),
      "c": np.array([int(data[i]) for i in range(4, len(data), 2)]),
    }
    instances.append(instance)
  return np.array(instances)

"""
Load solutions.
"""
def get_solutions(path):
  with open(path) as f:
    lines = f.readlines()
  
  solutions = [int(line.split()[2]) for line in lines]
  return np.array(solutions)
