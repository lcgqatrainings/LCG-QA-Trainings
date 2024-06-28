# test_assignment.py
import math

# Importing functions from the assignment file
from python.basics.day1_Assignment import calculate_area_of_circle, get_sphere_volume, difference_from_17, \
    within_100_of_1000_or_2000, sum_three_numbers, new_string_with_is, repeat_string, even_or_odd, count_fours, \
    repeat_first_two_chars, is_vowel


# Test cases for calculate_area_of_circle function
def test_calculate_area_of_circle():
    assert math.isclose(calculate_area_of_circle(1.1), 3.8013271108436504, rel_tol=1e-9)
    assert math.isclose(calculate_area_of_circle(0), 0, rel_tol=1e-9)
    assert math.isclose(calculate_area_of_circle(2), 12.566370614359172, rel_tol=1e-9)
    # Add more test cases as needed


# Test cases for get_sphere_volume function
def test_get_sphere_volume():
    assert math.isclose(get_sphere_volume(6), 904.7786842338603, rel_tol=1e-9)
    assert math.isclose(get_sphere_volume(0), 0, rel_tol=1e-9)
    assert math.isclose(get_sphere_volume(1), 4.1887902047863905, rel_tol=1e-9)
    # Add more test cases as needed


# Test cases for difference_from_17 function
def test_difference_from_17():
    assert difference_from_17(22) == 10
    assert difference_from_17(14) == 3
    assert difference_from_17(17) == 0
    # Add more test cases as needed


# Test cases for within_100_of_1000_or_2000 function
def test_within_100_of_1000_or_2000():
    assert within_100_of_1000_or_2000(950) == True
    assert within_100_of_1000_or_2000(1050) == True
    assert within_100_of_1000_or_2000(100) == False
    # Add more test cases as needed


# Test cases for sum_three_numbers function
def test_sum_three_numbers():
    assert sum_three_numbers(1, 2, 3) == 6
    assert sum_three_numbers(3, 3, 3) == 27
    assert sum_three_numbers(0, 0, 0) == 0
    # Add more test cases as needed


# Test cases for new_string_with_is function
def test_new_string_with_is():
    assert new_string_with_is("Array") == "IsArray"
    assert new_string_with_is("IsEmpty") == "IsEmpty"
    assert new_string_with_is("Test") == "IsTest"
    # Add more test cases as needed


# Test cases for repeat_string function
def test_repeat_string():
    assert repeat_string("abc", 2) == "abcabc"
    assert repeat_string("xyz", 3) == "xyzxyzxyz"
    assert repeat_string("a", 0) == ""
    # Add more test cases as needed


# Test cases for even_or_odd function
def test_even_or_odd():
    assert even_or_odd(10) == "10 is even"
    assert even_or_odd(3) == "3 is odd"
    assert even_or_odd(0) == "0 is even"
    # Add more test cases as needed


# Test cases for count_fours function
def test_count_fours():
    assert count_fours([1, 4, 6, 4, 7, 4]) == 3
    assert count_fours([1, 2, 3]) == 0
    assert count_fours([4, 4, 4, 4]) == 4
    # Add more test cases as needed


# Test cases for repeat_first_two_chars function
def test_repeat_first_two_chars():
    assert repeat_first_two_chars("abcdef", 3) == "ababab"
    assert repeat_first_two_chars("a", 3) == "aaa"
    assert repeat_first_two_chars("xy", 0) == ""
    # Add more test cases as needed


# Test cases for is_vowel function
def test_is_vowel():
    assert is_vowel("a") == True
    assert is_vowel("b") == False
    assert is_vowel("e") == True
    # Add more test cases as needed
