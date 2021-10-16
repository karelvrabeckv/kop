# Module tester

import constants as c
import loader as l
import solver as s

def run(algorithm, type, limit, path):
  results = []
  for n in c.NUM_OF_THINGS:
    if n > limit:
      break

    inst_file_path = path + str(n) + c.INST_FILE_PATH_POSTFIX
    instances = l.get_instances(inst_file_path)

    if (type == c.ALL_INSTANCES):
      if (algorithm == c.BF):
        result = s.solve_all(instances, c.BF)
      elif (algorithm == c.BF_BETTER):
        result = s.solve_all(instances, c.BF_BETTER)
      elif (algorithm == c.BB):
        result = s.solve_all(instances, c.BB)
      else:
        print("ERROR: wrong algorithm")
        return
    elif (type == c.RANDOM_INSTANCE):
      if (algorithm == c.BF):
        result = s.solve_random(instances, c.BF)
      elif (algorithm == c.BF_BETTER):
        result = s.solve_random(instances, c.BF_BETTER)
      elif (algorithm == c.BB):
        result = s.solve_random(instances, c.BB)
      else:
        print("ERROR: wrong algorithm")
        return
    else:
      print("ERROR: wrong type")
      return

    results.append(result)

    print("[N=" + str(n) + "]:", end=" ")
    print(str(result[1]) + " configurations, " + str(result[2]) + " ms")
  return results
