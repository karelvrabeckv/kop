# Module bf

"""
Solve the constructive form of the knapsack 
problem with BRUTE FORCE.
"""
def bf(M, w, c, curr_w = 0, curr_c = 0, curr_t = 0):
  # No more things to solve
  if curr_t == len(w):
    return curr_c if (curr_w <= M) else 0

  return max(
    bf(M, w, c, curr_w + w[curr_t], curr_c + c[curr_t], curr_t + 1), # Add
    bf(M, w, c, curr_w, curr_c, curr_t + 1) # Ignore
  )
