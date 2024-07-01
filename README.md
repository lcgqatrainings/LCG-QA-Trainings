## Scores

| Metric      | Count |
|-------------|-------|
| Total Tests | 49    |
| Passed      | 0     |
| Failures    | 49    |
| Errors      | 0     |
| Score       | 0.00% |

## Test Results

| Test Name                       | Status   | Assertion                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:--------------------------------|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| test_calculate_area_of_circle   | Failed   | def test_calculate_area_of_circle(): >    assert math.isclose(calculate_area_of_circle(1.1), 3.8013271108436504, rel_tol=1e-9) E    TypeError: must be real number, not NoneType tests/test_day1.py:12: TypeError                                                                                                                                                                                                                                               |
| test_get_sphere_volume          | Failed   | def test_get_sphere_volume(): >    assert math.isclose(get_sphere_volume(6), 904.7786842338603, rel_tol=1e-9) E    TypeError: must be real number, not NoneType tests/test_day1.py:20: TypeError                                                                                                                                                                                                                                                                |
| test_difference_from_17         | Failed   | def test_difference_from_17(): >    assert difference_from_17(22) == 10 E    assert None == 10 E    + where None = difference_from_17(22) tests/test_day1.py:28: AssertionError                                                                                                                                                                                                                                                                                 |
| test_within_100_of_1000_or_2000 | Failed   | def test_within_100_of_1000_or_2000(): >    assert within_100_of_1000_or_2000(950) == True E    assert None == True E    + where None = within_100_of_1000_or_2000(950) tests/test_day1.py:36: AssertionError                                                                                                                                                                                                                                                   |
| test_sum_three_numbers          | Failed   | def test_sum_three_numbers(): >    assert sum_three_numbers(1, 2, 3) == 6 E    assert None == 6 E    + where None = sum_three_numbers(1, 2, 3) tests/test_day1.py:44: AssertionError                                                                                                                                                                                                                                                                            |
| test_new_string_with_is         | Failed   | def test_new_string_with_is(): >    assert new_string_with_is("Array") == "IsArray" E    AssertionError: assert None == 'IsArray' E    + where None = new_string_with_is('Array') tests/test_day1.py:52: AssertionError                                                                                                                                                                                                                                         |
| test_repeat_string              | Failed   | def test_repeat_string(): >    assert repeat_string("abc", 2) == "abcabc" E    AssertionError: assert None == 'abcabc' E    + where None = repeat_string('abc', 2) tests/test_day1.py:60: AssertionError                                                                                                                                                                                                                                                        |
| test_even_or_odd                | Failed   | def test_even_or_odd(): >    assert even_or_odd(10) == "10 is even" E    AssertionError: assert None == '10 is even' E    + where None = even_or_odd(10) tests/test_day1.py:68: AssertionError                                                                                                                                                                                                                                                                  |
| test_count_fours                | Failed   | def test_count_fours(): >    assert count_fours([1, 4, 6, 4, 7, 4]) == 3 E    assert None == 3 E    + where None = count_fours([1, 4, 6, 4, 7, 4]) tests/test_day1.py:76: AssertionError                                                                                                                                                                                                                                                                        |
| test_repeat_first_two_chars     | Failed   | def test_repeat_first_two_chars(): >    assert repeat_first_two_chars("abcdef", 3) == "ababab" E    AssertionError: assert None == 'ababab' E    + where None = repeat_first_two_chars('abcdef', 3) tests/test_day1.py:84: AssertionError                                                                                                                                                                                                                       |
| test_is_vowel                   | Failed   | def test_is_vowel(): >    assert is_vowel("a") == True E    AssertionError: assert None == True E    + where None = is_vowel('a') tests/test_day1.py:92: AssertionError                                                                                                                                                                                                                                                                                         |
| test_calculate_triangle_area    | Failed   | def test_calculate_triangle_area(): >    assert calculate_triangle_area(10, 5) == 25.0 E    assert None == 25.0 E    + where None = calculate_triangle_area(10, 5) tests/test_day2.py:12: AssertionError                                                                                                                                                                                                                                                        |
| test_compute_gcd                | Failed   | def test_compute_gcd(): >    assert compute_gcd(48, 64) == 16 E    assert None == 16 E    + where None = compute_gcd(48, 64) tests/test_day2.py:20: AssertionError                                                                                                                                                                                                                                                                                              |
| test_compute_lcm                | Failed   | def test_compute_lcm(): >    assert compute_lcm(12, 15) == 60 E    assert None == 60 E    + where None = compute_lcm(12, 15) tests/test_day2.py:28: AssertionError                                                                                                                                                                                                                                                                                              |
| test_sum_three_numbers          | Failed   | def test_sum_three_numbers(): >    assert sum_three_numbers(1, 2, 3) == 6 E    assert None == 6 E    + where None = sum_three_numbers(1, 2, 3) tests/test_day2.py:36: AssertionError                                                                                                                                                                                                                                                                            |
| test_sum_two_integers           | Failed   | def test_sum_two_integers(): >    assert sum_two_integers(10, 5) == 20 E    assert None == 20 E    + where None = sum_two_integers(10, 5) tests/test_day2.py:44: AssertionError                                                                                                                                                                                                                                                                                 |
| test_check_values               | Failed   | def test_check_values(): >    assert check_values(10, 5) == True E    assert None == True E    + where None = check_values(10, 5) tests/test_day2.py:52: AssertionError                                                                                                                                                                                                                                                                                         |
| test_add_objects                | Failed   | def test_add_objects(): >    assert add_objects(10, 20) == 30 E    assert None == 30 E    + where None = add_objects(10, 20) tests/test_day2.py:60: AssertionError                                                                                                                                                                                                                                                                                              |
| test_display_personal_info      | Failed   | def test_display_personal_info(): >    assert display_personal_info("John", 25, "123 Main St") == "Name: John\nAge: 25\nAddress: 123 Main St" E    AssertionError: assert None == 'Name: John\nAge: 25\nAddress: 123 Main St' E    + where None = display_personal_info('John', 25, '123 Main St') tests/test_day2.py:68: AssertionError                                                                                                                        |
| test_compute_expression         | Failed   | def test_compute_expression(): >    assert compute_expression(4, 3) == 49 E    assert None == 49 E    + where None = compute_expression(4, 3) tests/test_day2.py:76: AssertionError                                                                                                                                                                                                                                                                             |
| test_compute_future_value       | Failed   | def test_compute_future_value(): >    assert math.isclose(compute_future_value(10000, 3.5, 7), 12722.79, rel_tol=1e-2) E    TypeError: must be real number, not NoneType tests/test_day2.py:84: TypeError                                                                                                                                                                                                                                                       |
| test_calculate_distance         | Failed   | def test_calculate_distance(): >    assert math.isclose(calculate_distance(1, 2, 4, 6), 5.0, rel_tol=1e-9) E    TypeError: must be real number, not NoneType tests/test_day2.py:92: TypeError                                                                                                                                                                                                                                                                   |
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
| test_print_numbers_while        | Failed   | capsys = <_pytest.capture.CaptureFixture object at 0x7f422097bb30>   def test_print_numbers_while(capsys):     print_numbers_while()     captured = capsys.readouterr() >    assert captured.out == "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n" E    AssertionError: assert '' == '1\n2\n3\n4\n...7\n8\n9\n10\n' E     E     - 1 E     - 2 E     - 3 E     - 4 E     - 5 E     - 6 E     - 7 E     - 8 E     - 9 E     - 10 tests/test_day4.py:61: AssertionError         |
| test_is_even_or_odd             | Failed   | def test_is_even_or_odd(): >    assert is_even_or_odd(4) == "Even" E    AssertionError: assert None == 'Even' E    + where None = is_even_or_odd(4) tests/test_day4.py:67: AssertionError                                                                                                                                                                                                                                                                       |
| test_print_even_numbers         | Failed   | capsys = <_pytest.capture.CaptureFixture object at 0x7f42209ad4c0>   def test_print_even_numbers(capsys):     print_even_numbers()     captured = capsys.readouterr() >    assert captured.out == "2\n4\n6\n8\n10\n12\n14\n16\n18\n20\n" E    AssertionError: assert '' == '2\n4\n6\n8\n...n16\n18\n20\n' E     E     - 2 E     - 4 E     - 6 E     - 8 E     - 10 E     - 12 E     - 14 E     - 16 E     - 18 E     - 20 tests/test_day4.py:77: AssertionError |
| test_check_positive             | Failed   | def test_check_positive(): >    assert check_positive(-5) == "Non-positive" E    AssertionError: assert None == 'Non-positive' E    + where None = check_positive(-5) tests/test_day4.py:83: AssertionError                                                                                                                                                                                                                                                     |
| test_basic_switch_case          | Failed   | def test_basic_switch_case(): >    assert basic_switch_case(1) == "One" E    AssertionError: assert None == 'One' E    + where None = basic_switch_case(1) tests/test_day4.py:91: AssertionError                                                                                                                                                                                                                                                                |
| test_skip_number_five           | Failed   | capsys = <_pytest.capture.CaptureFixture object at 0x7f42209fbd10>   def test_skip_number_five(capsys):     skip_number_five()     captured = capsys.readouterr() >    assert captured.out == "1\n2\n3\n4\n6\n7\n8\n9\n10\n" E    AssertionError: assert '' == '1\n2\n3\n4\n6\n7\n8\n9\n10\n' E     E     - 1 E     - 2 E     - 3 E     - 4 E     - 6 E     - 7 E     - 8 E     - 9 E     - 10 tests/test_day4.py:102: AssertionError                           |
| test_break_at_five              | Failed   | capsys = <_pytest.capture.CaptureFixture object at 0x7f42209f9e50>   def test_break_at_five(capsys):     break_at_five()     captured = capsys.readouterr() >    assert captured.out == "1\n2\n3\n4\n" E    AssertionError: assert '' == '1\n2\n3\n4\n' E     E     - 1 E     - 2 E     - 3 E     - 4 tests/test_day4.py:110: AssertionError                                                                                                                    |
| test_search_list                | Failed   | def test_search_list(): >    assert search_list([1, 2, 3, 4, 5], 3) == "Found" E    AssertionError: assert None == 'Found' E    + where None = search_list([1, 2, 3, 4, 5], 3) tests/test_day4.py:116: AssertionError                                                                                                                                                                                                                                           |
| test_end_program_if_negative    | Failed   | def test_end_program_if_negative():     # This is tricky to test as it exits the program     # One way is to mock sys.exit() in tests     import pytest >    with pytest.raises(SystemExit): E    Failed: DID NOT RAISE <class 'SystemExit'> tests/test_day4.py:127: Failed                                                                                                                                                                                     |
| test_total_distance             | Failed   | def test_total_distance(): >    assert total_distance(120, 150, 200) == 470 E    assert None == 470 E    + where None = total_distance(120, 150, 200) tests/test_variables.py:9: AssertionError                                                                                                                                                                                                                                                                 |
| test_distribute_candies         | Failed   | def test_distribute_candies(): >    assert distribute_candies(25, 4) == (6, 1) E    assert None == (6, 1) E    + where None = distribute_candies(25, 4) tests/test_variables.py:17: AssertionError                                                                                                                                                                                                                                                              |
| test_adjust_recipe              | Failed   | def test_adjust_recipe(): >    assert adjust_recipe(2, 8) == 4.0 E    assert None == 4.0 E    + where None = adjust_recipe(2, 8) tests/test_variables.py:25: AssertionError                                                                                                                                                                                                                                                                                     |
| test_total_cost                 | Failed   | def test_total_cost(): >    assert total_cost(100, 50, 75) == 225 E    assert None == 225 E    + where None = total_cost(100, 50, 75) tests/test_variables.py:33: AssertionError                                                                                                                                                                                                                                                                                |
| test_calculate_profit           | Failed   | def test_calculate_profit(): >    assert calculate_profit(1500, 1200) == 300 E    assert None == 300 E    + where None = calculate_profit(1500, 1200) tests/test_variables.py:41: AssertionError                                                                                                                                                                                                                                                                |
