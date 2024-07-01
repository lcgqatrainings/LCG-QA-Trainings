"""
Problem 1:
Write a Python program that calculates the area of a circle based on the radius entered by the user.

Example:
calculate_area_of_circle(1.1) should return 3.8013271108436504
"""
import math

def calculate_area_of_circle(radius):
    # Your code here
    return math.pi * radius ** 2
    pass


radius = 1.1
print(calculate_area_of_circle(radius))

#Method 2:
def calculate_area_of_circle(radius):
   area = 3.14 * radius ** 2
   return area

radius=1.1

print(calculate_area_of_circle(radius))
"""
Problem 2:
Write a Python program to get the volume of a sphere with radius six.

Example:
get_sphere_volume(6) should return 904.7786842338603
"""


def get_sphere_volume(radius):
    # Your code here
    sphere_volume = 4 / 3 * math.pi * radius ** 3
    return sphere_volume
    pass


radius = 6
sphere_volume = get_sphere_volume(radius)
print(sphere_volume)

#Method 2:
def get_sphere_volume(radius):
    volume=4/3*3.14159265359*radius**3
    return volume
radius=6
volume = get_sphere_volume(radius)
print(volume)


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
    if number > 17:
        difference = (number - 17) * 2
        return difference
    else:
        return 17 - number


number = int(input("enter a value:"))
difference = difference_from_17(number)
print(difference_from_17(number))

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
    if 1000-number<=100 or 2000-number<=100:
        return True
    else:
        return False
    pass
number=int(input("enter a value:"))
print(within_100_of_1000_or_2000(number))


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
    if a==b==c:
        return a**3
    else:
        return a+b+c
    pass


a = int(input("enter a value:"))
b = int(input("enter a value:"))
c = int(input("enter a value:"))
print(sum_three_numbers(a, b, c))

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
    if text[0:2]=="is":
        return text
    else:
        return "is"+text


text = input("enter a string:")
print(new_string_with_is(text))



"""
Problem 7:
Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

Example:
repeat_string("abc", 2) should return "abcabc"
repeat_string("xyz", 3) should return "xyzxyzxyz"
"""


def repeat_string(s, n):
    # Your code here
    if num>=0:
        return string*num
    else:
        return num
    pass


num = int(input("enter a value:"))
string = "test"
print(repeat_string(string,num))

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
    if num%2==0:
        return s1
    else:
        return s2
    pass


num = int(input("enter a value:"))
s1 = "number is even"
s2 = "number is odd"
print(even_or_odd(num))

"""
Problem 9:
Write a Python program to count the number 4 in a given list.

Example:
count_fours([1, 4, 6, 4, 7, 4]) should return 3
"""


def count_fours(lst):
    # Your code here
    return L1.count(4)
    pass


L1 = [3, 5, 4, 1, 6, 4, 4, 4]
print("count of fours:", count_fours(L1))

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
    if len(test) < 2:
        return test*num
    else:
        return test[0:2]*num
    pass

num=6
test=input("enter a string:")
print(repeat_first_two_chars(test,num))




"""
Problem 11:
Write a Python program to test whether a passed letter is a vowel or not.

Example:
is_vowel("a") should return True
is_vowel("b") should return False
"""


def is_vowel(char):
    # Your code here
   if i in L1:
       return True
   else:
       return False
   pass


L1 = ["a", "e", "i", "o", "u"]
i = input("enter a string:")
print(is_vowel(i))