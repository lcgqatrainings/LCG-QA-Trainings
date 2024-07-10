# test_assignment.py

# Importing functions from the assignment file
from python.intermediate.day6_Assignment import sum_lambda, multiply, sort_desc, greet, sqrt_lambda, apply_discount, \
    uppercase_lambda, power, reverse_strings_lambda, create_sentence


# Test cases for sum_lambda function
def test_sum_lambda():
    assert sum_lambda(3, 4) == 7
    assert sum_lambda(-1, 1) == 0
    assert sum_lambda(0, 0) == 0
    # Add more test cases as needed


# Test cases for multiply function
def test_multiply():
    assert multiply(x=3, y=4) == 12
    assert multiply(x=-1, y=5) == -5
    assert multiply(x=0, y=10) == 0
    # Add more test cases as needed


# Test cases for sort_desc lambda function
def test_sort_desc():
    assert sort_desc([3, 1, 4, 1, 5, 9]) == [9, 5, 4, 3, 1, 1]
    assert sort_desc([0, -1, -2, 2, 1]) == [2, 1, 0, -1, -2]
    assert sort_desc([]) == []
    # Add more test cases as needed


# Test cases for greet function
def test_greet():
    assert greet(name="Alice", message="Hello") == "Hello, Alice!"
    assert greet(name="Bob", message="Good morning") == "Good morning, Bob!"
    assert greet(name="Charlie", message="Hi") == "Hi, Charlie!"
    # Add more test cases as needed


# Test cases for sqrt_lambda function
def test_sqrt_lambda():
    assert sqrt_lambda(4) == 2.0
    assert sqrt_lambda(9) == 3.0
    assert sqrt_lambda(0) == 0.0
    # Add more test cases as needed


# Test cases for apply_discount function
def test_apply_discount():
    assert apply_discount(price=100, discount=10) == 90.0
    assert apply_discount(price=50, discount=20) == 40.0
    assert apply_discount(price=200, discount=0) == 200.0
    # Add more test cases as needed


# Test cases for uppercase_lambda function
def test_uppercase_lambda():
    assert uppercase_lambda("hello") == "HELLO"
    assert uppercase_lambda("world") == "WORLD"
    assert uppercase_lambda("") == ""
    # Add more test cases as needed


# Test cases for power function
def test_power():
    assert power(base=2, exponent=3) == 8
    assert power(base=5, exponent=0) == 1
    assert power(base=1, exponent=10) == 1
    # Add more test cases as needed


# Test cases for reverse_strings_lambda function
def test_reverse_strings_lambda():
    assert reverse_strings_lambda(["abc", "def"]) == ["cba", "fed"]
    assert reverse_strings_lambda(["hello", "world"]) == ["olleh", "dlrow"]
    assert reverse_strings_lambda([]) == []
    # Add more test cases as needed


# Test cases for create_sentence function
def test_create_sentence():
    assert create_sentence(subject="The cat", verb="chased", object="the mouse") == "The cat chased the mouse."
    assert create_sentence(subject="She", verb="reads", object="a book") == "She reads a book."
    assert create_sentence(subject="John", verb="is", object="tall") == "John is tall."
    # Add more test cases as needed
