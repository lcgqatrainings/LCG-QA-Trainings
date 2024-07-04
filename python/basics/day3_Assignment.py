"""
Problem 58:
Write a Python program to sum the first n positive integers.
Formula: Sum = n * (n + 1) / 2

Example:
sum_first_n_integers(5) should return 15
"""


def sum_first_n_integers(n):
   sum=n*(n+1)//2
   return sum
#print(sum_first_n_integers(5))



"""
Problem 59:
Write a Python program to convert height (in feet and inches) to centimeters.
Formula: 1 foot = 30.48 cm, 1 inch = 2.54 cm

Example:
convert_height_to_cm(5, 7) should return 170.18
"""


def convert_height_to_cm(feet, inches):
    feet_in_cm=feet*30.48
    inch_in_cm=inches*2.54
    height=feet_in_cm+inch_in_cm
    return height
#print(convert_height_to_cm(5,7))



"""
Problem 60:
Write a Python program to calculate the hypotenuse of a right-angled triangle.
Formula: Hypotenuse = sqrt(base^2 + height^2)

Example:
calculate_hypotenuse(3, 4) should return 5.0
"""

import math
def calculate_hypotenuse(base, height):
    Hypotenuse=math.sqrt(base**2+height**2)
    return Hypotenuse
#print(calculate_hypotenuse(3,4))


"""
Problem 61:
Write a Python program to convert the distance (in feet) to inches, yards, and miles.
Formulas: 1 foot = 12 inches, 1 foot = 0.333333 yard, 1 foot = 0.000189394 mile

Example:
convert_distance(5280) should return (63360, 1760, 1.0)
"""


def convert_distance(feet):
    distance_in_inches=round(feet*12)
    distance_in_yards=round(feet*0.333333)
    distance_in_miles=round(feet*0.000189394,1)
    return distance_in_inches,distance_in_yards,distance_in_miles
#print(convert_distance(5280))



"""
Problem 66:
Write a Python program to calculate the body mass index (BMI).
Formula: BMI = weight (kg) / height (m)^2

Example:
calculate_bmi(70, 1.75) should return 22.86
"""


def calculate_bmi(weight, height):
    BMI=round(weight/height**2,2)
    return BMI
#print(calculate_bmi(70,1.75))



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
    psi=kpa*0.145038
    mmHg=kpa*7.50062
    atm=kpa*0.00986923
    return psi,mmHg,atm
#print(convert_pressure(100))


"""
Problem 68:
Write a Python program to calculate the sum of digits of a number.

Example:
sum_of_digits(1234) should return 10
"""


def sum_of_digits(number):
    sum=0
    for digit in str(number):
        sum += int(digit)
    return sum

#print(sum_of_digits(1234))





