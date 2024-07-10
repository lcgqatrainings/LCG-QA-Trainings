# test_assignment.py

# Test cases for calculate_triangle_area function
def test_calculate_triangle_area():
    assert calculate_triangle_area(10, 5) == 25.0
    assert calculate_triangle_area(0, 5) == 0.0
    assert calculate_triangle_area(6, 7) == 21.0
    # Add more test cases as needed


# Test cases for compute_gcd function
def test_compute_gcd():
    assert compute_gcd(48, 64) == 16
    assert compute_gcd(54, 24) == 6
    assert compute_gcd(7, 13) == 1
    # Add more test cases as needed


# Test cases for compute_lcm function
def test_compute_lcm():
    assert compute_lcm(12, 15) == 60
    assert compute_lcm(7, 13) == 91
    assert compute_lcm(4, 5) == 20
    # Add more test cases as needed


# Test cases for sum_three_numbers function
def test_sum_three_numbers():
    assert sum_three_numbers(1, 2, 3) == 6
    assert sum_three_numbers(2, 2, 3) == 0
    assert sum_three_numbers(3, 3, 3) == 0
    # Add more test cases as needed


# Test cases for sum_two_integers function
def test_sum_two_integers():
    assert sum_two_integers(10, 5) == 20
    assert sum_two_integers(10, 2) == 12
    assert sum_two_integers(7, 8) == 20
    # Add more test cases as needed


# Test cases for check_values function
def test_check_values():
    assert check_values(10, 5) == True
    assert check_values(7, 2) == True
    assert check_values(3, 8) == False
    # Add more test cases as needed


# Test cases for add_objects function
def test_add_objects():
    assert add_objects(10, 20) == 30
    assert add_objects(10, "20") == None
    assert add_objects("10", 20) == None
    # Add more test cases as needed


# Test cases for display_personal_info function
def test_display_personal_info():
    assert display_personal_info("John", 25, "123 Main St") == "Name: John\nAge: 25\nAddress: 123 Main St"
    assert display_personal_info("Alice", 30, "456 Oak St") == "Name: Alice\nAge: 30\nAddress: 456 Oak St"
    assert display_personal_info("Bob", 40, "789 Pine St") == "Name: Bob\nAge: 40\nAddress: 789 Pine St"
    # Add more test cases as needed


# Test cases for compute_expression function
def test_compute_expression():
    assert compute_expression(4, 3) == 49
    assert compute_expression(1, 2) == 9
    assert compute_expression(0, 5) == 25
    # Add more test cases as needed


# Test cases for compute_future_value function
def test_compute_future_value():
    assert math.isclose(compute_future_value(10000, 3.5, 7), 12722.79, rel_tol=1e-2)
    assert math.isclose(compute_future_value(5000, 4, 10), 7401.22, rel_tol=1e-2)
    assert math.isclose(compute_future_value(2000, 5, 5), 2552.56, rel_tol=1e-2)
    # Add more test cases as needed


# Test cases for calculate_distance function
def test_calculate_distance():
    assert math.isclose(calculate_distance(1, 2, 4, 6), 5.0, rel_tol=1e-9)
    assert math.isclose(calculate_distance(0, 0, 3, 4), 5.0, rel_tol=1e-9)
    assert math.isclose(calculate_distance(-1, -1, 2, 3), 5.0, rel_tol=1e-9)
    # Add more test cases as needed
