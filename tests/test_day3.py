# test_assignment.py

# Importing functions from the assignment file
from python.basics.day3_Assignment import sum_first_n_integers, convert_height_to_cm, calculate_hypotenuse, \
    convert_distance, calculate_bmi, convert_pressure, sum_of_digits


# Test cases for sum_first_n_integers function
def test_sum_first_n_integers():
    assert sum_first_n_integers(5) == 15
    assert sum_first_n_integers(10) == 55
    assert sum_first_n_integers(1) == 1
    # Add more test cases as needed


# Test cases for convert_height_to_cm function
def test_convert_height_to_cm():
    assert convert_height_to_cm(5, 7) == 170.18
    assert convert_height_to_cm(6, 0) == 182.88
    assert convert_height_to_cm(4, 11) == 149.86
    # Add more test cases as needed


# Test cases for calculate_hypotenuse function
def test_calculate_hypotenuse():
    assert calculate_hypotenuse(3, 4) == 5.0
    assert calculate_hypotenuse(5, 12) == 13.0
    assert calculate_hypotenuse(8, 15) == 17.0
    # Add more test cases as needed


# Test cases for convert_distance function
def test_convert_distance():
    assert convert_distance(5280) == (63360, 1760, 1.0)
    assert convert_distance(1) == (12, 0.333333, 0.000189394)
    assert convert_distance(1000) == (12000, 333.333, 0.189394)
    # Add more test cases as needed


# Test cases for calculate_bmi function
def test_calculate_bmi():
    assert calculate_bmi(70, 1.75) == 22.86
    assert calculate_bmi(80, 1.8) == 24.69
    assert calculate_bmi(60, 1.6) == 23.44
    # Add more test cases as needed


# Test cases for convert_pressure function
def test_convert_pressure():
    assert convert_pressure(100) == (14.5038, 750.062, 0.986923)
    assert convert_pressure(200) == (29.0076, 1500.124, 1.973846)
    assert convert_pressure(50) == (7.2519, 375.031, 0.4934615)
    # Add more test cases as needed


# Test cases for sum_of_digits function
def test_sum_of_digits():
    assert sum_of_digits(1234) == 10
    assert sum_of_digits(0) == 0
    assert sum_of_digits(5678) == 26
    # Add more test cases as needed
