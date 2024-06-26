# test_assignment.py

# Importing functions from the assignment file
from python.variables.question1 import total_cost, total_distance, adjust_recipe, calculate_profit, distribute_candies


# Test cases for total_distance function
def test_total_distance():
    assert total_distance(120, 150, 200) == 470
    assert total_distance(0, 0, 0) == 0
    assert total_distance(100, 200, 300) == 600
    # Add more test cases as needed


# Test cases for distribute_candies function
def test_distribute_candies():
    assert distribute_candies(25, 4) == (6, 1)
    assert distribute_candies(100, 5) == (20, 0)
    assert distribute_candies(10, 3) == (3, 1)
    # Add more test cases as needed


# Test cases for adjust_recipe function
def test_adjust_recipe():
    assert adjust_recipe(2, 8) == 4.0
    assert adjust_recipe(0, 5) == 0.0
    assert adjust_recipe(1, 1) == 2.0
    # Add more test cases as needed


# Test cases for total_cost function
def test_total_cost():
    assert total_cost(100, 50, 75) == 225
    assert total_cost(0, 0, 0) == 0
    assert total_cost(10, 20, 30) == 60
    # Add more test cases as needed


# Test cases for calculate_profit function
def test_calculate_profit():
    assert calculate_profit(1500, 1200) == 300
    assert calculate_profit(0, 0) == 0
    assert calculate_profit(100, 200) == -100
    # Add more test cases as needed
