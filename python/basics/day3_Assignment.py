"""
Problem 58:
Write a Python program to sum the first n positive integers.
Formula: Sum = n * (n + 1) / 2

Example:
sum_first_n_integers(5) should return 15
"""


def sum_first_n_integers(n):
    # Your code here
    sum = n*(n+1)/2
    return sum
    pass
n = 5
print(sum_first_n_integers(n))

"""
Problem 59:
Write a Python program to convert height (in feet and inches) to centimeters.
Formula: 1 foot = 30.48 cm, 1 inch = 2.54 cm

Example:
convert_height_to_cm(5, 7) should return 170.18
"""


def convert_height_to_cm(feet, inches):
    # Your code here
   Centimeters = (Feet * 30.48) + (Inches * 2.54)
   return Centimeters

pass

Feet=5
Inches=7
print(convert_height_to_cm(Feet,Inches))

"""
Problem 60:
Write a Python program to calculate the hypotenuse of a right-angled triangle.
Formula: Hypotenuse = sqrt(base^2 + height^2)

Example:
calculate_hypotenuse(3, 4) should return 5.0
"""


def calculate_hypotenuse(base, height):
    # Your code here
    Hypotenuse = (base ** 2 + height ** 2)**0.5
    return Hypotenuse
    pass
base, height=3,4
print(calculate_hypotenuse(base,height))

"""
Problem 61:
Write a Python program to convert the distance (in feet) to inches, yards, and miles.
Formulas: 1 foot = 12 inches, 1 foot = 0.333333 yard, 1 foot = 0.000189394 mile

Example:
convert_distance(5280) should return (63360, 1760, 1.0)
"""


def convert_distance(feet):
    # Your code here
    distance_in_inches=foot*12*5280
    distance_in_yards=round(foot*0.33333*5280)
    distance_in_miles=round(foot*0.000189394*5280,1)
    return distance_in_inches,distance_in_yards,distance_in_miles
    pass
foot=1
print(convert_distance(foot))

"""
Problem 66:
Write a Python program to calculate the body mass index (BMI).
Formula: BMI = weight (kg) / height (m)^2

Example:
calculate_bmi(70, 1.75) should return 22.86
"""


def calculate_bmi(weight, height):
    # Your code here
    BMI =round( weight / height ** 2, 2)

    return BMI
    pass
weight,height=70,1.75
print(calculate_bmi(weight, height))

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
    # Your code here
    pressure_in_psi=0.145038*kpa*pressure
    pressure_in_mmHg=7.50062*kpa*pressure
    pressure_in_atm = 0.00986923 * kpa*pressure
    return pressure_in_psi,pressure_in_mmHg,pressure_in_atm
    pass

pressure=100
kpa=1
print(convert_pressure(kpa))
"""
Problem 68:
Write a Python program to calculate the sum of digits of a number.

Example:
sum_of_digits(1234) should return 10
"""


def sum_of_digits(number):
    # Your code here
    sum=int(num1[0])+int(num1[1])+int(num1[2])+int(num1[3])
    return sum
    pass
num = 1234
num1=str(1234)
print(sum_of_digits(num1))