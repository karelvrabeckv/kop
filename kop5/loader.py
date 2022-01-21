# Module loader

from os import listdir
from re import split

import constants as c
import numpy as np

"""
Load instances.
"""
def get_instances(path, keys, normalizer):
  # Read the folder
  files = listdir(c.INST_FOLDER + path)

  instances = {}
  for file in files:
    key = split("-0|\.", file)[1]
    if key not in keys:
      continue

    # Read the file
    with open(c.INST_FOLDER + path + "/" + file) as f:
      lines = f.readlines()

    clauses = []
    for line in lines:
      data = line.split()

      # Avoid EMPTY LINES and other
      # SPECIFIED CHARACTERS
      if not data or data[0] in ["c", "p"]:
        continue

      if data[0] == "w":
        # Get the WEIGHTS and LITERALS
        weights = list(map(int, data[1:-1]))
        w_sum = np.sum(weights)
        weights = [normalizer * (w / w_sum) for w in weights]
      else:
        # Get a CLAUSE
        clause = set()
        for num in data[:-1]:
          literal = int(num)
          if literal < 0:
            # The NEGATIVE literal
            clause.add((abs(literal), False))
          elif literal > 0:
            # The POSITIVE literal
            clause.add((literal, True))
        clauses.append(clause)

    # Save WEIGHTS, CLAUSES and
    # other data as the INSTANCE
    instances[key] = {
      c.NUM_OF_LITERALS: len(weights),
      c.SUM_OF_ORIGINAL_WEIGHTS: w_sum,
      c.WEIGHTS: np.array(weights),
      c.CLAUSES: np.array(clauses),
    }
  return instances

"""
Load solutions.
"""
def get_solutions(path, limit):
  # Read the file
  with open(c.SOL_FOLDER + path + "-opt.dat") as f:
    lines = f.readlines()
  
  solutions = {}
  for line in lines[0:limit]:
    data = line.split()
    key = split("-0", data[0])[1]
    solutions[key] = int(data[1])

  return solutions

"""
Load weights.
"""
def get_weights(path):
  # Read the folder
  files = listdir(c.INST_FOLDER + path)

  weights = []
  for file in files:
    # Read the file
    with open(c.INST_FOLDER + path + "/" + file) as f:
      lines = f.readlines()

    for line in lines:
      data = line.split()

      # Get WEIGHTS
      if data[0] == "w":
        weights += list(map(int, data[1:-1]))
        break

  return weights
