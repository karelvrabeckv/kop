# Module tester

from sa import sa

import loader as l
import numpy as np
import time as t

"""
Run all the tests.
"""
def run(file, start_temp, end_temp, cool_rate, inner_iters, limit = 500):
  parameters = {
    "start_temp": start_temp,
    "end_temp": end_temp,
    "cool_rate": cool_rate,
    "inner_iters": inner_iters,
  }

  instances = l.get_instances("instances/" + file)
  solutions = l.get_solutions("solutions/" + file)

  result = test_set(instances[0:limit], solutions[0:limit], parameters)

  print(
    "[" + file + "]",
    "AVG_TIME: " + str(result[1]) + " ms,",
    "MAX_TIME: " + str(result[2]) + " ms,",
    "AVG_ERROR: " + str(result[3]) + ",",
    "MAX_ERROR: " + str(result[4])
  )

  return result

"""
Test all the instances of the set.
"""
def test_set(instances, solutions, parameters):
  results = np.array([test_instance(i, s, parameters) for i, s in zip(instances, solutions)])

  avg_time, avg_error = np.mean(results, axis = 0)
  max_time, max_error = np.amax(results, axis = 0)

  return (results, avg_time, max_time, avg_error, max_error)

"""
Test an instance.
"""
def test_instance(instance, opt_cost, parameters):
  start = t.process_time() * 1000
  apr_cost = sa(instance, parameters)
  end = t.process_time() * 1000
  
  time_of_instance = end - start
  error_of_instance = abs(apr_cost - opt_cost) / max(apr_cost, opt_cost) if (apr_cost != opt_cost) else 0

  return (time_of_instance, error_of_instance)
