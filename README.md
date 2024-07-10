## Scores

| Metric      | Count |
|-------------|-------|
| Total Tests | 49    |
| Passed      | 25    |
| Failures    | 24    |
| Errors      | 0     |
| Score       | 51.02% |

## Test Results

| Test Name                       | Status   | Assertion                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:--------------------------------|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| test_calculate_area_of_circle   | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_get_sphere_volume          | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_difference_from_17         | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_within_100_of_1000_or_2000 | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_sum_three_numbers          | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_new_string_with_is         | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_repeat_string              | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_even_or_odd                | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_count_fours                | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_repeat_first_two_chars     | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_is_vowel                   | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_calculate_triangle_area    | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_compute_gcd                | Failed   | def test_compute_gcd(): >    assert compute_gcd(48, 64) == 16 E    assert (64, 48) == 16 E    + where (64, 48) = compute_gcd(48, 64) tests/test_day2.py:20: AssertionError                                                                                                                                                                                                                                                                                      |
| test_compute_lcm                | Failed   | def test_compute_lcm(): >    assert compute_lcm(12, 15) == 60 E    assert None == 60 E    + where None = compute_lcm(12, 15) tests/test_day2.py:28: AssertionError                                                                                                                                                                                                                                                                                              |
| test_sum_three_numbers          | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_sum_two_integers           | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_check_values               | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_add_objects                | Failed   | def test_add_objects(): >    assert add_objects(10, 20) == 30 E    assert None == 30 E    + where None = add_objects(10, 20) tests/test_day2.py:60: AssertionError                                                                                                                                                                                                                                                                                              |
| test_display_personal_info      | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_compute_expression         | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_compute_future_value       | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_calculate_distance         | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_sum_first_n_integers       | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_convert_height_to_cm       | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_calculate_hypotenuse       | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_convert_distance           | Failed   | def test_convert_distance(): >    assert convert_distance(5280) == (63360, 1760, 1.0) E    assert (63360, 1759.99824, 1.0) == (63360, 1760, 1.0) E     E     At index 1 diff: 1759.99824 != 1760 E     E     Full diff: E      ( E        63360, E     -   1760, E     +   1759.99824, E        1.0, E      ) tests/test_day3.py:34: AssertionError                                                                                                             |
| test_calculate_bmi              | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_convert_pressure           | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_sum_of_digits              | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_replicate_string           | Failed   | def test_replicate_string(): >    assert replicate_string("Hello", 3) == "HelloHelloHello" E    AssertionError: assert None == 'HelloHelloHello' E    + where None = replicate_string('Hello', 3) tests/test_day4.py:11: AssertionError                                                                                                                                                                                                                         |
| test_concatenate_strings        | Failed   | def test_concatenate_strings(): >    assert concatenate_strings("Alice", "Bob") == "AliceBob" E    AssertionError: assert None == 'AliceBob' E    + where None = concatenate_strings('Alice', 'Bob') tests/test_day4.py:19: AssertionError                                                                                                                                                                                                                      |
| test_contains_substring         | Failed   | def test_contains_substring(): >    assert contains_substring("Hello, world!", "world") == True E    AssertionError: assert None == True E    + where None = contains_substring('Hello, world!', 'world') tests/test_day4.py:27: AssertionError                                                                                                                                                                                                                 |
| test_string_to_int              | Failed   | def test_string_to_int(): >    assert string_to_int("123") == 123 E    AssertionError: assert None == 123 E    + where None = string_to_int('123') tests/test_day4.py:35: AssertionError                                                                                                                                                                                                                                                                        |
| test_list_length                | Failed   | def test_list_length(): >    assert list_length([1, 2, 3, 4, 5]) == 5 E    assert None == 5 E    + where None = list_length([1, 2, 3, 4, 5]) tests/test_day4.py:43: AssertionError                                                                                                                                                                                                                                                                              |
| test_increment_list             | Failed   | def test_increment_list(): >    assert increment_list([1, 2, 3]) == [2, 3, 4] E    assert None == [2, 3, 4] E    + where None = increment_list([1, 2, 3]) tests/test_day4.py:51: AssertionError                                                                                                                                                                                                                                                                 |
| test_print_numbers_while        | Failed   | capsys = <_pytest.capture.CaptureFixture object at 0x7fa6bb1c46b0>   def test_print_numbers_while(capsys):     print_numbers_while()     captured = capsys.readouterr() >    assert captured.out == "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n" E    AssertionError: assert '' == '1\n2\n3\n4\n...7\n8\n9\n10\n' E     E     - 1 E     - 2 E     - 3 E     - 4 E     - 5 E     - 6 E     - 7 E     - 8 E     - 9 E     - 10 tests/test_day4.py:61: AssertionError         |
| test_is_even_or_odd             | Failed   | def test_is_even_or_odd(): >    assert is_even_or_odd(4) == "Even" E    AssertionError: assert None == 'Even' E    + where None = is_even_or_odd(4) tests/test_day4.py:67: AssertionError                                                                                                                                                                                                                                                                       |
| test_print_even_numbers         | Failed   | capsys = <_pytest.capture.CaptureFixture object at 0x7fa6bb256cf0>   def test_print_even_numbers(capsys):     print_even_numbers()     captured = capsys.readouterr() >    assert captured.out == "2\n4\n6\n8\n10\n12\n14\n16\n18\n20\n" E    AssertionError: assert '' == '2\n4\n6\n8\n...n16\n18\n20\n' E     E     - 2 E     - 4 E     - 6 E     - 8 E     - 10 E     - 12 E     - 14 E     - 16 E     - 18 E     - 20 tests/test_day4.py:77: AssertionError |
| test_check_positive             | Failed   | def test_check_positive(): >    assert check_positive(-5) == "Non-positive" E    AssertionError: assert None == 'Non-positive' E    + where None = check_positive(-5) tests/test_day4.py:83: AssertionError                                                                                                                                                                                                                                                     |
| test_basic_switch_case          | Failed   | def test_basic_switch_case(): >    assert basic_switch_case(1) == "One" E    AssertionError: assert None == 'One' E    + where None = basic_switch_case(1) tests/test_day4.py:91: AssertionError                                                                                                                                                                                                                                                                |
| test_skip_number_five           | Failed   | capsys = <_pytest.capture.CaptureFixture object at 0x7fa6bb20a780>   def test_skip_number_five(capsys):     skip_number_five()     captured = capsys.readouterr() >    assert captured.out == "1\n2\n3\n4\n6\n7\n8\n9\n10\n" E    AssertionError: assert '' == '1\n2\n3\n4\n6\n7\n8\n9\n10\n' E     E     - 1 E     - 2 E     - 3 E     - 4 E     - 6 E     - 7 E     - 8 E     - 9 E     - 10 tests/test_day4.py:102: AssertionError                           |
| test_break_at_five              | Failed   | capsys = <_pytest.capture.CaptureFixture object at 0x7fa6bb20af00>   def test_break_at_five(capsys):     break_at_five()     captured = capsys.readouterr() >    assert captured.out == "1\n2\n3\n4\n" E    AssertionError: assert '' == '1\n2\n3\n4\n' E     E     - 1 E     - 2 E     - 3 E     - 4 tests/test_day4.py:110: AssertionError                                                                                                                    |
| test_search_list                | Failed   | def test_search_list(): >    assert search_list([1, 2, 3, 4, 5], 3) == "Found" E    AssertionError: assert None == 'Found' E    + where None = search_list([1, 2, 3, 4, 5], 3) tests/test_day4.py:116: AssertionError                                                                                                                                                                                                                                           |
| test_end_program_if_negative    | Failed   | def test_end_program_if_negative():     # This is tricky to test as it exits the program     # One way is to mock sys.exit() in tests     import pytest >    with pytest.raises(SystemExit): E    Failed: DID NOT RAISE <class 'SystemExit'> tests/test_day4.py:127: Failed                                                                                                                                                                                     |
| test_total_distance             | Failed   | def test_total_distance(): >    assert total_distance(120, 150, 200) == 470 E    assert None == 470 E    + where None = total_distance(120, 150, 200) tests/test_variables.py:9: AssertionError                                                                                                                                                                                                                                                                 |
| test_distribute_candies         | Failed   | def test_distribute_candies(): >    assert distribute_candies(25, 4) == (6, 1) E    assert None == (6, 1) E    + where None = distribute_candies(25, 4) tests/test_variables.py:17: AssertionError                                                                                                                                                                                                                                                              |
| test_adjust_recipe              | Failed   | def test_adjust_recipe(): >    assert adjust_recipe(2, 8) == 4.0 E    assert None == 4.0 E    + where None = adjust_recipe(2, 8) tests/test_variables.py:25: AssertionError                                                                                                                                                                                                                                                                                     |
| test_total_cost                 | Failed   | def test_total_cost(): >    assert total_cost(100, 50, 75) == 225 E    assert None == 225 E    + where None = total_cost(100, 50, 75) tests/test_variables.py:33: AssertionError                                                                                                                                                                                                                                                                                |
| test_calculate_profit           | Failed   | def test_calculate_profit(): >    assert calculate_profit(1500, 1200) == 300 E    assert None == 300 E    + where None = calculate_profit(1500, 1200) tests/test_variables.py:41: AssertionError                                                                                                                                                                                                                                                                |
