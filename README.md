## Scores

| Metric      | Count |
|-------------|-------|
| Total Tests | 49    |
| Passed      | 21    |
| Failures    | 28    |
| Errors      | 0     |
| Score       | 42.86% |

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
| test_compute_gcd                | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_compute_lcm                | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_sum_three_numbers          | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_sum_two_integers           | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_check_values               | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_add_objects                | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_display_personal_info      | Failed   | def test_display_personal_info(): >    assert display_personal_info("John", 25, "123 Main St") == "Name: John\nAge: 25\nAddress: 123 Main St" E    AssertionError: assert None == 'Name: John\nAge: 25\nAddress: 123 Main St' E    + where None = display_personal_info('John', 25, '123 Main St') tests/test_day2.py:68: AssertionError                                                                                                                        |
| test_compute_expression         | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_compute_future_value       | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_calculate_distance         | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| test_sum_first_n_integers       | Failed   | def test_sum_first_n_integers(): >    assert sum_first_n_integers(5) == 15 E    assert None == 15 E    + where None = sum_first_n_integers(5) tests/test_day3.py:10: AssertionError                                                                                                                                                                                                                                                                             |
| test_convert_height_to_cm       | Failed   | def test_convert_height_to_cm(): >    assert convert_height_to_cm(5, 7) == 170.18 E    assert None == 170.18 E    + where None = convert_height_to_cm(5, 7) tests/test_day3.py:18: AssertionError                                                                                                                                                                                                                                                               |
| test_calculate_hypotenuse       | Failed   | def test_calculate_hypotenuse(): >    assert calculate_hypotenuse(3, 4) == 5.0 E    assert None == 5.0 E    + where None = calculate_hypotenuse(3, 4) tests/test_day3.py:26: AssertionError                                                                                                                                                                                                                                                                     |
| test_convert_distance           | Failed   | def test_convert_distance(): >    assert convert_distance(5280) == (63360, 1760, 1.0) E    assert None == (63360, 1760, 1.0) E    + where None = convert_distance(5280) tests/test_day3.py:34: AssertionError                                                                                                                                                                                                                                                   |
| test_calculate_bmi              | Failed   | def test_calculate_bmi(): >    assert calculate_bmi(70, 1.75) == 22.86 E    assert None == 22.86 E    + where None = calculate_bmi(70, 1.75) tests/test_day3.py:42: AssertionError                                                                                                                                                                                                                                                                              |
| test_convert_pressure           | Failed   | def test_convert_pressure(): >    assert convert_pressure(100) == (14.5038, 750.062, 0.986923) E    assert None == (14.5038, 750.062, 0.986923) E    + where None = convert_pressure(100) tests/test_day3.py:50: AssertionError                                                                                                                                                                                                                                 |
| test_sum_of_digits              | Failed   | def test_sum_of_digits(): >    assert sum_of_digits(1234) == 10 E    assert None == 10 E    + where None = sum_of_digits(1234) tests/test_day3.py:58: AssertionError                                                                                                                                                                                                                                                                                            |
| test_replicate_string           | Failed   | def test_replicate_string(): >    assert replicate_string("Hello", 3) == "HelloHelloHello" E    AssertionError: assert None == 'HelloHelloHello' E    + where None = replicate_string('Hello', 3) tests/test_day4.py:11: AssertionError                                                                                                                                                                                                                         |
| test_concatenate_strings        | Failed   | def test_concatenate_strings(): >    assert concatenate_strings("Alice", "Bob") == "AliceBob" E    AssertionError: assert None == 'AliceBob' E    + where None = concatenate_strings('Alice', 'Bob') tests/test_day4.py:19: AssertionError                                                                                                                                                                                                                      |
| test_contains_substring         | Failed   | def test_contains_substring(): >    assert contains_substring("Hello, world!", "world") == True E    AssertionError: assert None == True E    + where None = contains_substring('Hello, world!', 'world') tests/test_day4.py:27: AssertionError                                                                                                                                                                                                                 |
| test_string_to_int              | Failed   | def test_string_to_int(): >    assert string_to_int("123") == 123 E    AssertionError: assert None == 123 E    + where None = string_to_int('123') tests/test_day4.py:35: AssertionError                                                                                                                                                                                                                                                                        |
| test_list_length                | Failed   | def test_list_length(): >    assert list_length([1, 2, 3, 4, 5]) == 5 E    assert None == 5 E    + where None = list_length([1, 2, 3, 4, 5]) tests/test_day4.py:43: AssertionError                                                                                                                                                                                                                                                                              |
| test_increment_list             | Failed   | def test_increment_list(): >    assert increment_list([1, 2, 3]) == [2, 3, 4] E    assert None == [2, 3, 4] E    + where None = increment_list([1, 2, 3]) tests/test_day4.py:51: AssertionError                                                                                                                                                                                                                                                                 |
| test_print_numbers_while        | Failed   | capsys = <_pytest.capture.CaptureFixture object at 0x7f5657dd5fd0>   def test_print_numbers_while(capsys):     print_numbers_while()     captured = capsys.readouterr() >    assert captured.out == "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n" E    AssertionError: assert '' == '1\n2\n3\n4\n...7\n8\n9\n10\n' E     E     - 1 E     - 2 E     - 3 E     - 4 E     - 5 E     - 6 E     - 7 E     - 8 E     - 9 E     - 10 tests/test_day4.py:61: AssertionError         |
| test_is_even_or_odd             | Failed   | def test_is_even_or_odd(): >    assert is_even_or_odd(4) == "Even" E    AssertionError: assert None == 'Even' E    + where None = is_even_or_odd(4) tests/test_day4.py:67: AssertionError                                                                                                                                                                                                                                                                       |
| test_print_even_numbers         | Failed   | capsys = <_pytest.capture.CaptureFixture object at 0x7f5657dd7500>   def test_print_even_numbers(capsys):     print_even_numbers()     captured = capsys.readouterr() >    assert captured.out == "2\n4\n6\n8\n10\n12\n14\n16\n18\n20\n" E    AssertionError: assert '' == '2\n4\n6\n8\n...n16\n18\n20\n' E     E     - 2 E     - 4 E     - 6 E     - 8 E     - 10 E     - 12 E     - 14 E     - 16 E     - 18 E     - 20 tests/test_day4.py:77: AssertionError |
| test_check_positive             | Failed   | def test_check_positive(): >    assert check_positive(-5) == "Non-positive" E    AssertionError: assert None == 'Non-positive' E    + where None = check_positive(-5) tests/test_day4.py:83: AssertionError                                                                                                                                                                                                                                                     |
| test_basic_switch_case          | Failed   | def test_basic_switch_case(): >    assert basic_switch_case(1) == "One" E    AssertionError: assert None == 'One' E    + where None = basic_switch_case(1) tests/test_day4.py:91: AssertionError                                                                                                                                                                                                                                                                |
| test_skip_number_five           | Failed   | capsys = <_pytest.capture.CaptureFixture object at 0x7f5657d8aff0>   def test_skip_number_five(capsys):     skip_number_five()     captured = capsys.readouterr() >    assert captured.out == "1\n2\n3\n4\n6\n7\n8\n9\n10\n" E    AssertionError: assert '' == '1\n2\n3\n4\n6\n7\n8\n9\n10\n' E     E     - 1 E     - 2 E     - 3 E     - 4 E     - 6 E     - 7 E     - 8 E     - 9 E     - 10 tests/test_day4.py:102: AssertionError                           |
| test_break_at_five              | Failed   | capsys = <_pytest.capture.CaptureFixture object at 0x7f5657d8c9b0>   def test_break_at_five(capsys):     break_at_five()     captured = capsys.readouterr() >    assert captured.out == "1\n2\n3\n4\n" E    AssertionError: assert '' == '1\n2\n3\n4\n' E     E     - 1 E     - 2 E     - 3 E     - 4 tests/test_day4.py:110: AssertionError                                                                                                                    |
| test_search_list                | Failed   | def test_search_list(): >    assert search_list([1, 2, 3, 4, 5], 3) == "Found" E    AssertionError: assert None == 'Found' E    + where None = search_list([1, 2, 3, 4, 5], 3) tests/test_day4.py:116: AssertionError                                                                                                                                                                                                                                           |
| test_end_program_if_negative    | Failed   | def test_end_program_if_negative():     # This is tricky to test as it exits the program     # One way is to mock sys.exit() in tests     import pytest >    with pytest.raises(SystemExit): E    Failed: DID NOT RAISE <class 'SystemExit'> tests/test_day4.py:127: Failed                                                                                                                                                                                     |
| test_total_distance             | Failed   | def test_total_distance(): >    assert total_distance(120, 150, 200) == 470 E    assert None == 470 E    + where None = total_distance(120, 150, 200) tests/test_variables.py:9: AssertionError                                                                                                                                                                                                                                                                 |
| test_distribute_candies         | Failed   | def test_distribute_candies(): >    assert distribute_candies(25, 4) == (6, 1) E    assert None == (6, 1) E    + where None = distribute_candies(25, 4) tests/test_variables.py:17: AssertionError                                                                                                                                                                                                                                                              |
| test_adjust_recipe              | Failed   | def test_adjust_recipe(): >    assert adjust_recipe(2, 8) == 4.0 E    assert None == 4.0 E    + where None = adjust_recipe(2, 8) tests/test_variables.py:25: AssertionError                                                                                                                                                                                                                                                                                     |
| test_total_cost                 | Failed   | def test_total_cost(): >    assert total_cost(100, 50, 75) == 225 E    assert None == 225 E    + where None = total_cost(100, 50, 75) tests/test_variables.py:33: AssertionError                                                                                                                                                                                                                                                                                |
| test_calculate_profit           | Failed   | def test_calculate_profit(): >    assert calculate_profit(1500, 1200) == 300 E    assert None == 300 E    + where None = calculate_profit(1500, 1200) tests/test_variables.py:41: AssertionError                                                                                                                                                                                                                                                                |
