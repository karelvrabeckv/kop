# Module dynamic

"""
Solve the constructive form of the knapsack 
problem with DYNAMIC PROGRAMMING.
"""
def dynamic(n, M, w, c):
  global results
  results = [['x' for _ in range(n + 1)] for _ in range(M + 1)]
  return run(M, w, c)

def run(M, w, c, curr_w = 0, curr_t = 0):
  global results

  # No more things to solve
  if curr_t == len(w):
    return 0

  # Check the weight limit
  if curr_w + w[curr_t] > M:
    ignored = run(M, w, c, curr_w, curr_t + 1)
    results[curr_w][curr_t] = ignored
    return ignored

  # Add current thing
  if results[curr_w + w[curr_t]][curr_t + 1] != 'x':
    added = results[curr_w + w[curr_t]][curr_t + 1]
  else:
    added = run(M, w, c, curr_w + w[curr_t], curr_t + 1)

  # Ignore current thing
  if results[curr_w][curr_t + 1] != 'x':
    ignored = results[curr_w][curr_t + 1]
  else:
    ignored = run(M, w, c, curr_w, curr_t + 1)
  
  result = max(added + c[curr_t], ignored)
  results[curr_w][curr_t] = result
  return result
