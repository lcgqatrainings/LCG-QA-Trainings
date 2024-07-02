"""
Problem 58:
Write a Python program to sum the first n positive integers.
Formula: Sum = n * (n + 1) / 2

Example:
sum_first_n_integers(5) should return 15
"""


def sum_first_n_integers(n):
    # Your code here
    pass


"""
Problem 59:
Write a Python program to convert height (in feet and inches) to centimeters.
Formula: 1 foot = 30.48 cm, 1 inch = 2.54 cm

Example:
convert_height_to_cm(5, 7) should return 170.18
"""


def convert_height_to_cm(feet, inches):
    # Your code here
    pass


"""
Problem 60:
Write a Python program to calculate the hypotenuse of a right-angled triangle.
Formula: Hypotenuse = sqrt(base^2 + height^2)

Example:
calculate_hypotenuse(3, 4) should return 5.0
"""


def calculate_hypotenuse(base, height):
    # Your code here
    pass


"""
Problem 61:
Write a Python program to convert the distance (in feet) to inches, yards, and miles.
Formulas: 1 foot = 12 inches, 1 foot = 0.333333 yard, 1 foot = 0.000189394 mile

Example:
convert_distance(5280) should return (63360, 1760, 1.0)
"""


def convert_distance(feet):
    # Your code here
    pass


"""
Problem 66:
Write a Python program to calculate the body mass index (BMI).
Formula: BMI = weight (kg) / height (m)^2

Example:
calculate_bmi(70, 1.75) should return 22.86
"""


def calculate_bmi(weight, height):
    # Your code here
    pass


"""
Problem 67:
Write a Python program to convert pressure in kilopascals to pounds per square inch (psi), millimeters of mercury (mmHg), and atmosphere pressure (atm).
Formulas: 
1 kPa = 0.145038 psi
1 kPa = 7.50062 mmHg
1 kPa = 0.00986923 atm

Example:
convert_pressure(100) should return (14.5038, 750.062, 0.986923)
"""


def convert_pressure(kpa):
    pressure=((0.145038*kpa),(7.50062*kpa),(0.00986923*kpa))
    return pressure

"""
Problem 68:
Write a Python program to calculate the sum of digits of a number.

Example:
sum_of_digits(1234) should return 10
"""


def sum_of_digits(number):
    sum = 0
    while number != 0:
        digit = number % 10
        sum = sum + digit
        number = number // 10
    print(sum)
sum_of_digits(1234)