# Module gr

"""
Solve the constructive form of the knapsack 
problem with GREEDY HEURISTIC.
"""
def gr(M, w, c):
  ratios = []
  for i in range(len(c)):
    ratios.append((c[i], w[i], c[i] / w[i]))
  ratios = sorted(ratios, key = lambda x: x[2], reverse = True)

  curr_c = curr_w = 0
  for thing in ratios:
    # Check the weight limit
    if curr_w + thing[1] > M:
      continue

    curr_c += thing[0]
    curr_w += thing[1]
  return curr_c
