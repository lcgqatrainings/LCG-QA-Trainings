"""
Problem 1:
Write a Python program that calculates the area of a circle based on the radius entered by the user.

Example:
calculate_area_of_circle(1.1) should return 3.8013271108436504
"""
import math
def calculate_area_of_circle(radius):
    # Your code here
    a = math.pi*radius**2
    print(a)
calculate_area_of_circle(5)

"""
Problem 2:
Write a Python program to get the volume of a sphere with radius six.
Example:
get_sphere_volume(6) should return 904.7786842338603
"""


def get_sphere_volume(radius):
    v = 4/3*math.pi*radius**3
    print(v)
get_sphere_volume(6)


"""
Problem 3:
Write a Python program to calculate the difference between a given number and 17. 
If the number is greater than 17, return twice the absolute difference.

Example:
difference_from_17(22) should return 10
difference_from_17(14) should return 3
"""


def difference_from_17(a):
    # Your code here
    diff = a - 17
    if diff >= 0:
        print(2*diff)
    else:
        print(diff)


difference_from_17(49)


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
    if number in range(900,1100):
        print(True)
    elif number in range(1900,2100):
        print(True)
    else:
        print(False)


within_100_of_1000_or_2000(777)


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
    if a == b == c:
        print(3 * a)
    else:
        print(a + b + c)


sum_three_numbers(3,4,7)
sum_three_numbers(3,3,3)



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
    if s.startswith("is"):
        print(s)
    elif s.startswith("Is"):
        print(s)
    elif s.startswith("IS"):
        print(s)
    elif s.startswith("iS"):
        print(s)
    else:
        print("Is", s, sep="")


new_string_with_is("Kamal")


"""
Problem 7:
Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

Example:
repeat_string("abc", 2) should return "abcabc"
repeat_string("xyz", 3) should return "xyzxyzxyz"
"""


def repeat_string(s, n):
    # Your code here
    if n > 0:
        print(s * n)
    else:
        print("n Should be a +ve values and should be an integer")

repeat_string('kamal', 1)


"""
Problem 8:
Write a Python program that determines whether a given number (accepted from the user) is even or odd, 
and prints an appropriate message to the user.

Example:
even_or_odd(10) should return "10 is even"
even_or_odd(3) should return "3 is odd"
"""

number=int(input("Enter an number "))
def even_or_odd(number):
    # Your code here
    if number % 2 == 0:
        print(number, " is an Even number")
    else:
        print(number, " is an odd number")


even_or_odd(number)

"""
Problem 9:
Write a Python program to count the number 4 in a given list.

Example:
count_fours([1, 4, 6, 4, 7, 4]) should return 3
"""
lst = [2,4,4,3,2,5,5,4,8,9]

def count_fours(lst):
    # Your code here
    count = 0
    for i in range(len(lst)):
        if lst[i] == 4:
            count = count + 1
    print("The count of number of 4's in the list is ", count)

count_fours(lst)


"""
Problem 10:
Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. 
Return n copies of the whole string if the length is less than 2.

Example:
repeat_first_two_chars("abcdef", 3) should return "ababab"
repeat_first_two_chars("a", 3) should return "aaa"
"""

a = input("Enter a string ")
def repeat_first_two_chars(s, n):
    # Your code
    if n > 0 and len(a) > 2:
        print(n * (a[0] + a[1]))
    else:
        print(n * a)


repeat_first_two_chars('hello', 5)


"""
Problem 11:
Write a Python program to test whether a passed letter is a vowel or not.

Example:
is_vowel("a") should return True
is_vowel("b") should return False
"""

char= input("Input an alphabet ")
def is_vowel(char):
    # Your code here
    if char in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
        print(char, " is Vowel")
    else:
        print(char, " is not a Vowel")


is_vowel(char)
