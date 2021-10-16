# Module decisive_knapsack_bf

"""
Solve the decision form of the knapsack problem
with BRUTE FORCE.
"""
def decisive_knapsack_bf(w, c, max_w, min_c):
  global timer
  timer = 0
  return (run(w, c, max_w, min_c), timer)

def run(w, c, max_w, min_c, curr_w = 0, curr_c = 0, curr_t = 0):
  # No more things to solve
  if (curr_t == len(w)):
    global timer
    timer = timer + 1
    return True if (curr_w <= max_w and curr_c >= min_c) else False

  return (
    # Add this thing to the knapsack
    run(w, c, max_w, min_c, curr_w + w[curr_t], curr_c + c[curr_t], curr_t + 1)
    or
    # Ignore this thing
    run(w, c, max_w, min_c, curr_w, curr_c, curr_t + 1)
  )
