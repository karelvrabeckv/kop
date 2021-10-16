# Module solver

from decisive_knapsack_bb import decisive_knapsack_bb
from decisive_knapsack_bf_better import decisive_knapsack_bf_better
from decisive_knapsack_bf import decisive_knapsack_bf
from random import randrange

import constants as c
import time as t

# Solve all instances of the set
def solve_all(instances, algorithm):
  results = []
  configurations = 0
  start = t.process_time() * 1000
  for i in instances:
    result = solve(i, algorithm)
    configurations = configurations + result[1]
    results.append(result)
  end = t.process_time() * 1000
  time = end - start
  return (results, configurations, time)

# Solve a random instance of the set
def solve_random(instances, algorithm):
  i = instances[randrange(len(instances))]
  return solve(i, algorithm)

# Solve an instance
def solve(i, algorithm):
  start = t.process_time() * 1000
  if (algorithm == c.BF):
    result = decisive_knapsack_bf(i["weights"], i["costs"], i["maxWeight"], i["minCost"])
  elif (algorithm == c.BF_BETTER):
    result = decisive_knapsack_bf_better(i["weights"], i["costs"], i["maxWeight"], i["minCost"])
  elif (algorithm == c.BB):
    result = decisive_knapsack_bb(i["weights"], i["costs"], i["maxWeight"], i["minCost"])
  else:
    print("ERROR: wrong algorithm")
  end = t.process_time() * 1000
  time = end - start
  return (*result, time)
