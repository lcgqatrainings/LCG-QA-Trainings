"""
Problem 30:
Write a Python program that will accept the base and height of a triangle and compute its area.
Formula: Area = 0.5 * base * height

Example:
calculate_triangle_area(10, 5) should return 25.0
"""
import math


def calculate_triangle_area(base, height):
    return 0.5 * base * height


"""
Problem 31:
Write a Python program that computes the greatest common divisor (GCD) of two positive integers.

Example:
compute_gcd(48, 64) should return 16
"""


def compute_gcd(x, y):
    gcd = 1
    for i in range(1, x + 1 if x < y else y + 1):
        if x % i == 0 and y % i == 0 and gcd <= i:
            gcd = i
    return gcd


"""
Problem 32:
Write a Python program to find the least common multiple (LCM) of two positive integers.
Formula: LCM(a, b) = abs(a*b) // GCD(a, b)

Example:
compute_lcm(12, 15) should return 60
"""


def compute_lcm(x, y):
    gcd = compute_gcd(x, y)
    lcm = x * y // gcd
    return lcm


"""
Problem 33:
Write a Python program to sum three given integers. However, if two values are equal, the sum will be zero.

Example:
sum_three_numbers(1, 2, 3) should return 6
sum_three_numbers(2, 2, 3) should return 0
"""


def sum_three_numbers(a, b, c):
    if a == b or b == c or c==a:
        return 0
    else:
        return a + b + c


"""
Problem 34:
Write a Python program to sum two given integers. However, if the sum is between 15 and 20 it will return 20.

Example:
sum_two_integers(10, 5) should return 20
sum_two_integers(10, 2) should return 12
"""


def sum_two_integers(a, b):
    if a + b in range(15,21):
        return 20
    else:
        return a + b


"""
Problem 35:
Write a Python program that returns true if the two given integer values are equal or their sum or difference is 5.

Example:
check_values(10, 5) should return True
check_values(7, 2) should return True
check_values(3, 8) should return False
"""


def check_values(a, b):
    if a == b or a + b == 5 or a - b ==5:
        return True
    else:
        return False


"""
Problem 36:
Write a Python program to add two objects if both objects are integers.

Example:
add_objects(10, 20) should return 30
add_objects(10, "20") should return None
"""


def add_objects(a, b):
    if isinstance(a,int) and isinstance(b,int):
        return a + b
    else:
        return None


"""
Problem 37:
Write a Python program that displays your name, age, and address on three different lines.

Example:
display_personal_info("John", 25, "123 Main St")
Output:
Name: John
Age: 25
Address: 123 Main St
"""


def display_personal_info(name, age, address):
    return f"Name: {name}\nAge: {age}\nAddress: {address}"


"""
Problem 38:
Write a Python program to solve (x + y) * (x + y).
Test Data : x = 4, y = 3
Expected Output : (4 + 3) ^ 2 = 49

Example:
compute_expression(4, 3) should return 49
"""


def compute_expression(x, y):
    return (x + y) ** 2


"""
Problem 39:
Write a Python program to compute the future value of a specified principal amount, rate of interest, 
and number of years.
Formula: Future Value = P * (1 + r / 100) ** t

Example:
compute_future_value(10000, 3.5, 7) should return 12722.79
"""


def compute_future_value(principal, rate, years):
    return round((principal * (1 + rate / 100) ** years), 2)


"""
Problem 40:
Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).
Formula: Distance = sqrt((x2 - x1)**2 + (y2 - y1)**2)

Example:
calculate_distance(1, 2, 4, 6) should return 5.0
"""


def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
