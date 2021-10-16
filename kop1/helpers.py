# Module helpers

def getMaxTime(data, type):
  times = []
  if (type == "configurations"):
    for i in data:
      times.append(i[1])
  elif (type == "time"):
    for i in data:
      times.append(i[2])
  else:
    print("ERROR: wrong type")
    return
  return max(times)

def getAverageTime(value):
  return value / 500
