# Module redux

"""
Solve the constructive form of the knapsack 
problem with MODIFIED GREEDY.
"""
def redux(M, w, c):
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

  costs = []
  for i in range(len(c)):
    if w[i] <= M:
      costs.append(c[i])
  max_cost = 0 if (not len(costs)) else max(costs)

  return curr_c if (curr_c > max_cost) else max_cost
