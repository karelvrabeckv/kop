# Module fptas

"""
Solve the constructive form of the knapsack 
problem with FPTAS.
"""
def fptas(n, M, w, c, e):
  new_c = []
  for i in range(len(w)):
    if w[i] <= M:
      new_c.append(c[i])
  if not len(new_c):
    return 0
  C_M = max(new_c)
  K = (e * C_M) / n
  if K < 1:
    K = 1
  modified_c = []
  for i in range(len(c)):
    modified_c.append(int(c[i] // K))

  global results
  results = [[float("inf") for _ in range(n + 1)] for _ in range(sum(modified_c) + 1)]
  results[0][0] = 0

  things = run(n, M, w, modified_c)
  apr_cost = 0
  for i in range(len(things)):
    apr_cost += things[i] * c[i]
  return apr_cost

def run(n, M, w, c):
  global results

  max_cost = 0
  for j in range(1, n + 1): # Columns
    for i in range(len(results)): # Rows
      # Avoid useless iterations
      if i > sum(c[0:j]):
        break

      # Compute the weight
      results[i][j] = min(
        results[i][j - 1],
        results[i - c[j - 1]][j - 1] + w[j - 1] if (i - c[j - 1] >= 0) else float("inf")
      )
      
      # Compute the cost
      if j == n and i > max_cost and results[i][j] <= M:
        max_cost = i
  
  # Collect the things
  things = []
  for j in range(n, 0, -1):
    if results[max_cost][j] == results[max_cost][j - 1]:
      things.insert(0, 0)
    else:
      things.insert(0, 1)
      max_cost -= c[j - 1]

  return things
