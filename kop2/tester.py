# Module tester

import constants as c
import helpers as h
import loader as l
import timeit as t

from algorithms.bb import bb
from algorithms.dynamic import dynamic
from algorithms.greedy import greedy
from algorithms.redux import redux
from algorithms.fptas import fptas

"""
Run all the tests.
"""
def run(algorithm, path, limit = 40, e = 1.0):
  results = []
  for n in c.NUM_OF_THINGS:
    if n > limit:
      break

    # Load instances and solutions
    instances = l.get_instances(path + str(n))
    solutions = l.get_solutions(path + str(n))

    # Solve the instances
    if algorithm == c.BB:
      result = test_set(instances, solutions, c.BB)
    elif algorithm == c.DYNAMIC:
      result = test_set(instances, solutions, c.DYNAMIC)
    elif algorithm == c.GREEDY:
      result = test_set(instances, solutions, c.GREEDY)
    elif algorithm == c.REDUX:
      result = test_set(instances, solutions, c.REDUX)
    elif algorithm == c.FPTAS:
      result = test_set(instances, solutions, c.FPTAS, e)
    else:
      print("ERROR: wrong algorithm")
      return

    print("[N=" + str(n) + "] ", end="")
    print("TIME: " + str(result[1]) + " ms, ", end="")
    print("AVG_TIME: " + str(result[2]) + " ms, ", end="")
    print("MAX_TIME: " + str(result[3]) + " ms, ", end="")
    print("ERRORS: " + str(result[4]) + "/" + str(len(instances)) + ", ", end="")
    print("AVG_ERROR: " + str(result[5]) + ", ", end="")
    print("MAX_ERROR: " + str(result[6]))

    results.append(result)
  return results

"""
Test all the instances of the set.
"""
def test_set(instances, solutions, algorithm, e = 1.0):
  results = []
  for i in range(len(instances)):
    result = test_instance(instances[i], solutions[i], algorithm, e)
    results.append(result)

  time_of_set, avg_time, max_time = h.getTimeData(results)
  errors_of_set, avg_error, max_error = h.getErrorData(results)

  return (results, time_of_set, avg_time, max_time, errors_of_set, avg_error, max_error)

"""
Test an instance.
"""
def test_instance(instance, solution, algorithm, e):
  opt_cost = solution["C"]

  if algorithm == c.BB:
    apr_cost = bb(instance["M"], instance["w"], instance["c"])
    stmt, setup = c.BB_STMT, c.BB_SETUP
  elif algorithm == c.DYNAMIC:
    apr_cost = dynamic(instance["n"], instance["M"], instance["w"], instance["c"])
    stmt, setup = c.DYNAMIC_STMT, c.DYNAMIC_SETUP
  elif algorithm == c.GREEDY:
    apr_cost = greedy(instance["M"], instance["w"], instance["c"])
    stmt, setup = c.GREEDY_STMT, c.GREEDY_SETUP
  elif algorithm == c.REDUX:
    apr_cost = redux(instance["M"], instance["w"], instance["c"])
    stmt, setup = c.REDUX_STMT, c.REDUX_SETUP
  elif algorithm == c.FPTAS:
    apr_cost = fptas(instance["n"], instance["M"], instance["w"], instance["c"], e)
    stmt, setup = c.FPTAS_STMT, c.FPTAS_SETUP

  time_of_instance = t.timeit(stmt = stmt, setup = setup, number = 1, globals = locals()) * 1000
  error_of_instance = abs(apr_cost - opt_cost) / max(apr_cost, opt_cost) if (apr_cost != opt_cost) else 0

  return (apr_cost, time_of_instance, error_of_instance)
