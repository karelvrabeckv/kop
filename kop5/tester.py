# Module tester

from sa import sa

import constants as c
import loader as l
import numpy as np
import time as t

"""
Run all the tests.
"""
def run(start_temp, end_temp, cool_rate, inner_iters, penalizer, path, limit, normalizer):
  params = {
    c.START_TEMP: start_temp,
    c.END_TEMP: end_temp,
    c.COOL_RATE: cool_rate,
    c.INNER_ITERS: inner_iters,
    c.PENALIZER: penalizer,
  }

  solutions = l.get_solutions(path, limit)
  instances = l.get_instances(path, solutions.keys(), normalizer)

  result = test_set(instances, solutions, normalizer, params)
  print(
    "[" + path + "]",
    "AVG_TIME: " + format(result[1], ".3f") + " ms,",
    "MAX_TIME: " + format(result[2], ".3f") + " ms,",
    "AVG_ERROR: " + str(result[3]) + ",",
    "MAX_ERROR: " + str(result[4])
  )
  return result

"""
Test all the instances of the set.
"""
def test_set(instances, solutions, normalizer, params):
  results = np.array([
    test_instance(instances[key], solutions[key], normalizer, params) for key in instances.keys()
  ], dtype = "object")

  times = np.array([result[0] for result in results])
  errors = np.array([result[1] for result in results])

  avg_time, max_time = np.mean(times), np.amax(times)
  avg_error, max_error = np.mean(errors), np.amax(errors)

  return (results, avg_time, max_time, avg_error, max_error)

"""
Test an instance.
"""
def test_instance(instance, solution, normalizer, params):
  start = t.process_time() * 1000
  w_log, apr_w = sa(instance, params)
  end = t.process_time() * 1000
  
  opt_w = normalizer * (solution / instance[c.SUM_OF_ORIGINAL_WEIGHTS])
  time_of_instance = end - start
  error_of_instance = abs(apr_w - opt_w) / max(apr_w, opt_w)

  return (time_of_instance, error_of_instance, w_log, opt_w)
