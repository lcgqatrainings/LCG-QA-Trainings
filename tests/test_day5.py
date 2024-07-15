# test_assignment.py

# Importing functions from the assignment file
from python.basics.day5_Assignment import square, is_palindrome, factorial, fibonacci, is_even, product, apply_function, \
    filter_even_numbers, greater_than_ten, sort_list, apply_lambda


# Test cases for square function
def test_square():
    assert square(4) == 16
    assert square(0) == 0
    assert square(-3) == 9
    # Add more test cases as needed


# Test cases for is_palindrome function
def test_is_palindrome():
    assert is_palindrome("madam") == True
    assert is_palindrome("hello") == False
    assert is_palindrome("racecar") == True
    # Add more test cases as needed


# Test cases for factorial function
def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    assert factorial(1) == 1
    # Add more test cases as needed


# Test cases for fibonacci function
def test_fibonacci():
    assert fibonacci(7) == 13
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    # Add more test cases as needed


# Test cases for is_even function
def test_is_even():
    assert is_even(4) == True
    assert is_even(7) == False
    assert is_even(0) == True
    # Add more test cases as needed


# Test cases for lambda function product
def test_product():
    assert product(3, 4) == 12
    assert product(0, 5) == 0
    assert product(-3, 3) == -9
    # Add more test cases as needed


# Test cases for apply_function function
def test_apply_function():
    def increment(x):
        return x + 1

    assert apply_function(increment, 5) == 6
    assert apply_function(increment, 0) == 1
    assert apply_function(increment, -1) == 0
    # Add more test cases as needed


# Test cases for filter_even_numbers function
def test_filter_even_numbers():
    assert filter_even_numbers([1, 2, 3, 4, 5]) == [2, 4]
    assert filter_even_numbers([2, 4, 6, 8]) == [2, 4, 6, 8]
    assert filter_even_numbers([1, 3, 5, 7]) == []
    # Add more test cases as needed


# Test cases for lambda function greater_than_ten
def test_greater_than_ten():
    assert greater_than_ten(15) == True
    assert greater_than_ten(5) == False
    assert greater_than_ten(10) == False
    # Add more test cases as needed


# Test cases for sort_list function
def test_sort_list():
    assert sort_list([3, 1, 4, 1, 5, 9]) == [1, 1, 3, 4, 5, 9]
    assert sort_list([0, -1, -2, 2, 1]) == [-2, -1, 0, 1, 2]
    assert sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
    # Add more test cases as needed


# Test cases for apply_lambda function
def test_apply_lambda():
    assert apply_lambda(lambda x: x * 2, [1, 2, 3]) == [2, 4, 6]
    assert apply_lambda(lambda x: x + 1, [0, -1, -2]) == [1, 0, -1]
    assert apply_lambda(lambda x: x ** 2, [1, 2, 3]) == [1, 4, 9]
    # Add more test cases as needed
