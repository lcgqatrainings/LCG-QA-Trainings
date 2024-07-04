## Scores

| Metric      | Count |
|-------------|-------|
| Total Tests | 49    |
| Passed      | 43    |
| Failures    | 6     |
| Errors      | 0     |
| Score       | 87.76% |

## Test Results

| Test Name                       | Status   | Assertion                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:--------------------------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| test_calculate_area_of_circle   | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_get_sphere_volume          | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_difference_from_17         | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_within_100_of_1000_or_2000 | Failed   | def test_within_100_of_1000_or_2000(): >    assert within_100_of_1000_or_2000(950) == True E    assert None == True E    + where None = within_100_of_1000_or_2000(950) tests/test_day1.py:36: AssertionError                                                                                                                                                                                                                                      |
| test_sum_three_numbers          | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_new_string_with_is         | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_repeat_string              | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_even_or_odd                | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_count_fours                | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_repeat_first_two_chars     | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_is_vowel                   | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_calculate_triangle_area    | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_compute_gcd                | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_compute_lcm                | Failed   | def test_compute_lcm(): >    assert compute_lcm(12, 15) == 60 E    assert None == 60 E    + where None = compute_lcm(12, 15) tests/test_day2.py:28: AssertionError                                                                                                                                                                                                                                                                                 |
| test_sum_three_numbers          | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_sum_two_integers           | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_check_values               | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_add_objects                | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_display_personal_info      | Failed   | def test_display_personal_info(): >    assert display_personal_info("John", 25, "123 Main St") == "Name: John\nAge: 25\nAddress: 123 Main St" E    AssertionError: assert 'Name: John \...: 123 Main St' == 'Name: John\n...: 123 Main St' E     E     - Name: John E     + Name: John E     ?      + E     - Age: 25 E     + Age: 25 E     ?    + E      Address: 123 Main St tests/test_day2.py:68: AssertionError                               |
| test_compute_expression         | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_compute_future_value       | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_calculate_distance         | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_sum_first_n_integers       | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_convert_height_to_cm       | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_calculate_hypotenuse       | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_convert_distance           | Failed   | def test_convert_distance():     assert convert_distance(5280) == (63360, 1760, 1.0) >    assert convert_distance(1) == (12, 0.333333, 0.000189394) E    assert (12, 0, 0.0) == (12, 0.333333, 0.000189394) E     E     At index 1 diff: 0 != 0.333333 E     E     Full diff: E      ( E        12, E     -   0.333333, E     -   0.000189394, E     +   0, E     +   0.0, E      ) tests/test_day3.py:35: AssertionError                          |
| test_calculate_bmi              | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_convert_pressure           | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_sum_of_digits              | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_replicate_string           | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_concatenate_strings        | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_contains_substring         | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_string_to_int              | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_list_length                | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_increment_list             | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_print_numbers_while        | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_is_even_or_odd             | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_print_even_numbers         | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_check_positive             | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_basic_switch_case          | Failed   | def test_basic_switch_case(): >    assert basic_switch_case(1) == "One" E    AssertionError: assert None == 'One' E    + where None = basic_switch_case(1) tests/test_day4.py:91: AssertionError                                                                                                                                                                                                                                                   |
| test_skip_number_five           | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_break_at_five              | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_search_list                | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_end_program_if_negative    | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_total_distance             | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_distribute_candies         | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_adjust_recipe              | Failed   | def test_adjust_recipe():     assert adjust_recipe(2, 8) == 4.0 >    assert adjust_recipe(0, 5) == 0.0 tests/test_variables.py:26: _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _  original_sugar = 0, people_served = 5   def adjust_recipe(original_sugar, people_served): >    return people_served / original_sugar E    ZeroDivisionError: division by zero python/basics/question1.py:54: ZeroDivisionError |
| test_total_cost                 | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| test_calculate_profit           | Passed   |                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
