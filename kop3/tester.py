# Module tester

from algorithms.bb import bb
from algorithms.bf import bf
from algorithms.dp import dp
from algorithms.gr import gr
from constants import (
  DATA_FOLDER,
  BF, BB, DP, GR,
  BF_STMT, BB_STMT, DP_STMT, GR_STMT,
  BF_SETUP, BB_SETUP, DP_SETUP, GR_SETUP,
)
from helpers import (
  get_instances,
  get_time_data,
  get_error_data,
)
from os import listdir
from timeit import timeit

"""
Run all the tests.
"""
def run(alg, folder):
  files = listdir(DATA_FOLDER + "/" + folder)
  results = []

  for file in files:
    # Load instances
    instances = get_instances(DATA_FOLDER + "/" + folder + "/" + file)

    # Solve the instances
    if alg == BF:
      result = test_set(instances, BF)
    elif alg == BB:
      result = test_set(instances, BB)
    elif alg == DP:
      result = test_set(instances, DP)
    elif alg == GR:
      result = test_set(instances, GR)
    else:
      print("[ERROR] Wrong algorithm.")
      return

    print("[" + folder + "/" + file + "] ", end = "")
    print("TIME: " + str(result[1]) + " ms, ", end = "")
    print("AVG_TIME: " + str(result[2]) + " ms, ", end = "")
    print("MAX_TIME: " + str(result[3]) + " ms, ", end = "")
    print("ERRORS: " + str(result[4]) + "/" + str(len(instances)) + ", ", end = "")
    print("AVG_ERROR: " + str(result[5]) + ", ", end = "")
    print("MAX_ERROR: " + str(result[6]))

    results.append(result)

  return results

"""
Test all the instances of the set.
"""
def test_set(instances, alg):
  results = []

  for instance in instances:
    result = test_instance(instance, alg)
    results.append(result)

  time_of_set, avg_time, max_time = get_time_data(results)
  errors_of_set, avg_error, max_error = get_error_data(results)

  return (results, time_of_set, avg_time, max_time, errors_of_set, avg_error, max_error)

"""
Test an instance.
"""
def test_instance(instance, alg):
  error_of_instance = 0

  if alg == BF:
    apr_cost = bf(instance["M"], instance["w"], instance["c"])
    stmt, setup = BF_STMT, BF_SETUP
  elif alg == BB:
    apr_cost = bb(instance["M"], instance["w"], instance["c"])
    stmt, setup = BB_STMT, BB_SETUP
  elif alg == DP:
    apr_cost = dp(instance["n"], instance["M"], instance["w"], instance["c"])
    stmt, setup = DP_STMT, DP_SETUP
  elif alg == GR:
    apr_cost = gr(instance["M"], instance["w"], instance["c"])
    stmt, setup = GR_STMT, GR_SETUP

    opt_cost = dp(instance["n"], instance["M"], instance["w"], instance["c"])
    error_of_instance = abs(apr_cost - opt_cost) / max(apr_cost, opt_cost) if (apr_cost != opt_cost) else 0

  time_of_instance = timeit(stmt = stmt, setup = setup, number = 1, globals = locals()) * 1000

  return (apr_cost, time_of_instance, error_of_instance)
