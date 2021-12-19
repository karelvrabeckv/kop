# Module sa

import numpy as np

"""
Solve the constructive form of the knapsack 
problem with SIMULATED ANNEALING.
"""
def sa(inst, params):
  t = params["start_temp"]
  best = state = np.zeros(inst["n"], bool)

  # Cool down the temperature
  while t > params["end_temp"]:
    # Achieve the equilibrium
    iters = params["inner_iters"]
    while iters:
      state = get_neighbour(state, inst, t)
      if get_cost(state, inst) > get_cost(best, inst):
        best = state
      iters -= 1
    t *= params["cool_rate"]

  return get_cost(best, inst)

"""
Choose a neighbour randomly.
"""
def get_neighbour(state, inst, t):
  # Construct the neighbour
  neighbour = np.array([*state])
  neighbour[np.random.randint(0, inst["n"])] ^= True

  state_cost = get_cost(state, inst)
  neighbour_cost = get_cost(neighbour, inst)

  # The neighbour is better
  if neighbour_cost > state_cost:
    return neighbour
  
  # The neighbour can also be better
  delta = state_cost - neighbour_cost
  if np.random.rand() < np.exp(-delta / t):
    return neighbour

  return state

"""
Calculate the cost.
"""
def get_cost(conf, inst):
  # The heavier weight over the limit,
  # the more negative cost
  total_weight = np.sum(inst["w"], where = conf)
  if total_weight > inst["M"]:
    return inst["M"] - total_weight

  return np.sum(inst["c"], where = conf)
