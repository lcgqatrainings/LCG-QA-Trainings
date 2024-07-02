"""
Problem 1:
Write a Python program that calculates the area of a circle based on the radius entered by the user.

Example:
calculate_area_of_circle(1.1) should return 3.8013271108436504
"""
import math


def calculate_area_of_circle(radius):
    # Your code here
    result = math.pi * radius ** 2
    print(" calculate_area_of_circle(1.1) is: ", result)
    return result

"""
Problem 2:
Write a Python program to get the volume of a sphere with radius six.

Example:
get_sphere_volume(6) should return 904.7786842338603
"""


def get_sphere_volume(radius):
    # Your code here
    sphere = (4/3)*(radius ** 3 * math.pi)
    return sphere
    # print(" get_sphere_volume(6) is: ", get_sphere_volume(6))

"""
Problem 3:
Write a Python program to calculate the difference between a given number and 17.
If the number is greater than 17, return twice the absolute difference.

Example:
difference_from_17(22) should return 10
difference_from_17(14) should return 3
"""


def difference_from_17(number):
    # Your code here
    if number <= 17:
        return 17 - number
    else:
        return (number - 17) * 2


# print("difference_from_17(22) is: ", difference_from_17(22))
# print("difference_from_17(14) is: ", difference_from_17(14))




"""
Problem 4:
Write a Python program to test whether a number is within 100 of 1000 or 2000.

Example:
within_100_of_1000_or_2000(950) should return True
within_100_of_1000_or_2000(1050) should return True
within_100_of_1000_or_2000(100) should return False
"""

def within_100_of_1000_or_2000(number):
    # Your code here
    if number in range(101, 2000):
        return True
    elif number <= 100:
        return False

# print("within_100_of_1000_or_2000(950) is: ", within_100_of_1000_or_2000(950))
# print("within_100_of_1000_or_2000(1050) is: ", within_100_of_1000_or_2000(1050))
# print("within_100_of_1000_or_2000(100) is: ", within_100_of_1000_or_2000(100))

"""
Problem 5:
Write a Python program to calculate the sum of three given numbers.
If the values are equal, return three times their sum.

Example:
sum_three_numbers(1, 2, 3) should return 6
sum_three_numbers(3, 3, 3) should return 27
"""


def sum_three_numbers(a, b, c):
    # Your code here
    x = a + b + c
    if a == b == c:
        x = x * 3
    # print("sum_three_numbers(1, 2, 3) is: ", sum_three_numbers(1, 2, 3))
    # print("sum_three_numbers(3, 3, 3) is: ", sum_three_numbers(3, 3, 3))
    return x
"""
Problem 6:
Write a Python program to get a newly-generated string from a given string where "Is" has been added to the front.
Return the string unchanged if the given string already begins with "Is".

Example:
new_string_with_is("Array") should return "IsArray"
new_string_with_is("IsEmpty") should return "IsEmpty"
"""


def new_string_with_is(s):
    # Your code here
    if 'Is' in s:
        text = s
        return text
    else:
        text = 'Is' + s
        return text

# print("new_string_with_is(Array) is: ", new_string_with_is("Array"))
# print("new_string_with_is(IsEmpty) is: ", new_string_with_is("IsEmpty"))

pass


"""
Problem 7:
Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

Example:
repeat_string("abc", 2) should return "abcabc"
repeat_string("xyz", 3) should return "xyzxyzxyz"
"""


def repeat_string(s, n):
    # Your code here
    result = ""
    for i in range(n):
        result = result + s
    # print("repeat_string(abc, 2) is: ", repeat_string("abc", 2))
    # print("repeat_string(xyz, 3) is: ", repeat_string("xyz", 3))
    return result

# a= (s*n)
# return a

"""
Problem 8:
Write a Python program that determines whether a given number (accepted from the user) is even or odd,
and prints an appropriate message to the user.

Example:
even_or_odd(10) should return "10 is even"
even_or_odd(3) should return "3 is odd"
"""


def even_or_odd(number):
    # Your code here
    mod = int(number) % 2
    if mod > 0:
        res = " is odd"

    else:
        res = " is even"
    return str(number) + res


# print("even_or_odd(10) is: ", even_or_odd(10))
# print("even_or_odd(3) is: ", even_or_odd(3))

pass


"""
Problem 9:
Write a Python program to count the number 4 in a given list.

Example:
count_fours([1, 4, 6, 4, 7, 4]) should return 3
"""


def count_fours(lst):
    # Your code here
    count = 0
    for n in lst:
        if n == 4:
            count = count + 1
    return count
# print("count_fours([1, 4, 6, 4, 7, 4]) is: ", count_fours([1, 4, 6, 4, 7, 4]))
pass


"""
Problem 10:
Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string.
Return n copies of the whole string if the length is less than 2.

Example:
repeat_first_two_chars("abcdef", 3) should return "ababab"
repeat_first_two_chars("a", 3) should return "aaa"
"""


def repeat_first_two_chars(s, n):
    # Your code here
    flen = 2
    if flen > len(s):
        flen = len(s)
    substr = s[:flen]
    result = ""
    for i in range(n):
        result = result + substr
    return result

# print("repeat_first_two_chars(abcdef, 3) is: ", repeat_first_two_chars("abcdef", 3))
# print("repeat_first_two_chars(a, 3) is: ", repeat_first_two_chars("a", 3))
pass


"""
Problem 11:
Write a Python program to test whether a passed letter is a vowel or not.

Example:
is_vowel("a") should return True
is_vowel("b") should return False
"""


def is_vowel(char):
    # Your code here
    if char in ('a', 'e', 'i', 'o', 'u'):
        stmt = True
    else:
        stmt = False
    return stmt


# print("is_vowel(a) is: ", is_vowel("a"))
# print("is_vowel(b) is: ", is_vowel("b"))
pass
