# Module bb

"""
Solve the constructive form of the knapsack 
problem with BRANCH & BOUND.
"""
def bb(M, w, c):
  global opt_cost
  opt_cost = 0
  return run(M, w, c)

def run(M, w, c, curr_w = 0, curr_c = 0, curr_t = 0):
  global opt_cost

  # No more things to solve
  if curr_t == len(w):
    # Check the optimality
    if curr_c > opt_cost:
      opt_cost = curr_c
    return curr_c

  # Check the cost limit
  c_sum = 0
  for i in range(curr_t, len(c)):
    c_sum = c_sum + c[i]
  if curr_c + c_sum < opt_cost:
    return curr_c

  # Check the weight limit
  if curr_w + w[curr_t] > M:
    return run(M, w, c, curr_w, curr_c, curr_t + 1) # Ignore

  return max(
    run(M, w, c, curr_w + w[curr_t], curr_c + c[curr_t], curr_t + 1), # Add
    run(M, w, c, curr_w, curr_c, curr_t + 1) # Ignore
  )
