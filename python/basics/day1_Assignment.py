"""
Problem 1:
Write a Python program that calculates the area of a circle based on the radius entered by the user.

Example:
calculate_area_of_circle(1.1) should return 3.8013271108436504
"""
import math

def calculate_area_of_circle(radius):
    aoc = 2*3.14*(radius)**2
    print(aoc)
    # Your code here
    pass
calculate_area_of_circle(5)

"""
Problem 2:
Write a Python program to get the volume of a sphere with radius six.

Example:
get_sphere_volume(6) should return 904.7786842338603
"""
# def volume():
# volume = 1.34*3.14*6*6*6
# print(volume)

def get_sphere_volume(radius):
    spherevolume = 1.33*3.14*math.sqrt(radius)*radius
    print(spherevolume)
    pass
get_sphere_volume(2)

"""
Problem 3:
Write a Python program to calculate the difference between a given number and 17. 
If the number is greater than 17, return twice the absolute difference.

Example:
difference_from_17(22) should return 10
difference_from_17(14) should return 3
"""


def difference_from_17(number):
    if number<=17:
        print(17-number)
    else:
     print((number-17)*2)
    pass

difference_from_17(22)
difference_from_17(14)

"""
Problem 4:
Write a Python program to test whether a number is within 100 of 1000 or 2000.

Example:
within_100_of_1000_or_2000(950) should return True
within_100_of_1000_or_2000(1050) should return True
within_100_of_1000_or_2000(100) should return False
"""


def within_100_of_1000_or_2000(number):

    pass


"""
Problem 5:
Write a Python program to calculate the sum of three given numbers. 
If the values are equal, return three times their sum.

Example:
sum_three_numbers(1, 2, 3) should return 6
sum_three_numbers(3, 3, 3) should return 27
"""
def sum_three_numbers(a, b, c):

   if a == b == c:
      print(3*(a+b+c))
   else:
       print(a+b+c)

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
     if s.startswith("Is"):
         print(s)
     else:
        print ("Is" + s )
pass
new_string_with_is("ANU")
new_string_with_is("Is spandana")



"""
Problem 7:
Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

Example:
repeat_string("abc", 2) should return "abcabc"
repeat_string("xyz", 3) should return "xyzxyzxyz"
"""
def repeat_string(s, n):
    print(s*n)
    pass
repeat_string("spandu",4)

"""
Problem 8:
Write a Python program that determines whether a given number (accepted from the user) is even or odd, 
and prints an appropriate message to the user.

Example:
even_or_odd(10) should return "10 is even"
even_or_odd(3) should return "3 is odd"
"""


def even_or_odd(number):
    if number%2==0:
        print("even number")
    else:
        print("odd number")
    pass
even_or_odd(6)

"""
Problem 9:
Write a Python program to count the number 4 in a given list.

Example:
count_fours([1, 4, 6, 4, 7, 4]) should return 3
"""
def count_fours(lst):
    print(lst.count(7))
    pass

count_fours([1, 4, 6, 4, 7, 4])

"""
Problem 10:
Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. 
Return n copies of the whole string if the length is less than 2.

Example:
repeat_first_two_chars("abcdef", 3) should return "ababab"
repeat_first_two_chars("a", 3) should return "aaa"
"""


def repeat_first_two_chars(s, n):
    if len(s)<=2:
        print(s*n)
    else:
        print((s[:2])*2)
    pass
repeat_first_two_chars("spandu",2)
"""
Problem 11:
Write a Python program to test whether a passed letter is a vowel or not.

Example:
is_vowel("a") should return True
is_vowel("b") should return False
"""


def is_vowel(char):
    vowels="aeiouAEIOU"
    ans=char in vowels
    print(ans)
pass
is_vowel('A')
is_vowel('b')
