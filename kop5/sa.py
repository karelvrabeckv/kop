# Module sa

import constants as c
import numpy as np

"""
Solve the SAT with SIMULATED ANNEALING.
"""
def sa(inst, params):
  t = params[c.START_TEMP]
  state = get_init_state(inst)
  best_w = state_w = get_weight(state, inst, params)
  w_log = []
  step = 0
  
  while t > params[c.END_TEMP]:
    for _ in range(8 * inst[c.NUM_OF_LITERALS]):
      step += 1

      state, state_w = get_neighbour(state, state_w, inst, params, t)
      if state_w > best_w:
        best_w = state_w

      w_log.append((step, state_w))
    t *= params[c.COOL_RATE]

  return (w_log, best_w)

"""
Set an initial state.
"""
def get_init_state(inst):
  return np.random.randint(2, size = inst[c.NUM_OF_LITERALS], dtype = bool)

"""
Choose a random neighbour.
"""
def get_neighbour(state, state_w, inst, params, t):
  neighbour = np.array([*state])
  neighbour[np.random.randint(0, inst[c.NUM_OF_LITERALS])] ^= True
  neighbour_w = get_weight(neighbour, inst, params)

  if neighbour_w > state_w:
    return (neighbour, neighbour_w)
  
  delta = state_w - neighbour_w
  if np.random.rand() < np.exp(-delta / t):
    return (neighbour, neighbour_w)

  return (state, state_w)

"""
Get the weight of the configuration.
"""
def get_weight(conf, inst, params):
  weight = np.sum(inst[c.WEIGHTS], where = conf)
  num_of_unsat = get_num_of_unsat(conf, inst)

  return weight / (1 + num_of_unsat / params[c.PENALIZER])

"""
Get the number of unsatisfied clauses.
"""
def get_num_of_unsat(conf, inst):
  num_of_unsat = 0

  for clause in inst[c.CLAUSES]:
    satisfiable = False

    for literal in clause:
      outer_eval = literal[1]
      inner_eval = conf[literal[0] - 1]

      if (outer_eval == inner_eval):
        satisfiable = True
        break

    if not satisfiable:
      num_of_unsat += 1
    
  return num_of_unsat
