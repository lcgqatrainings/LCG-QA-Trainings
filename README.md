## Scores

| Metric      | Count |
|-------------|-------|
| Total Tests | 1     |
| Passed      | 0     |
| Failures    | 0     |
| Errors      | 1     |
| Score       | 0.00% |

## Test Results

| Test Name       | Status   | Assertion                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:----------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| tests.test_day1 | Error    | /opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/_pytest/python.py:492: in importtestmodule   mod = import_path( /opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/_pytest/pathlib.py:591: in import_path   importlib.import_module(module_name) /opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/importlib/__init__.py:90: in import_module   return _bootstrap._gcd_import(name[level:], package, level) <frozen importlib._bootstrap>:1387: in _gcd_import   ??? <frozen importlib._bootstrap>:1360: in _find_and_load   ??? <frozen importlib._bootstrap>:1331: in _find_and_load_unlocked   ??? <frozen importlib._bootstrap>:935: in _load_unlocked   ??? /opt/hostedtoolcache/Python/3.12.4/x64/lib/python3.12/site-packages/_pytest/assertion/rewrite.py:178: in exec_module   exec(co, module.__dict__) tests/test_day1.py:5: in <module>   from python.basics.day1_Assignment import calculate_area_of_circle, get_sphere_volume, difference_from_17, \ E   File "/home/runner/work/LCG-QA-Trainings/LCG-QA-Trainings/python/basics/day1_Assignment.py", line 47 E    if number=number-17: E     ^^^^^^^^^^^^^^^^ E  SyntaxError: invalid syntax. Maybe you meant '==' or ':=' instead of '='? |
