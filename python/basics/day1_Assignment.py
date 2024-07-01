"""
Problem 1:
Write a Python program that calculates the area of a circle based on the radius entered by the user.

Example:
calculate_area_of_circle(1.1) should return 3.8013271108436504
"""
import math
def calculate_area_of_circle(radius):
    print(math.pi*(radius**2))


r = float(input("Enter radius: "))
calculate_area_of_circle(r)


"""
Problem 2:
Write a Python program to get the volume of a sphere with radius six.

Example:
get_sphere_volume(6) should return 904.7786842338603
"""


def get_sphere_volume(radius):
    print(math.pi*(4/3)*(radius**2))


radius = float(input("Enter radius: "))
get_sphere_volume(radius)


"""
Problem 3:
Write a Python program to calculate the difference between a given number and 17. 
If the number is greater than 17, return twice the absolute difference.

Example:
difference_from_17(22) should return 10
difference_from_17(14) should return 3
"""


def difference_from_17(number):
     if number > 17:
         return (number-17)+(number-17)
     else:
         return 17-number

n = int(input("Enter number: "))
print(difference_from_17(n))


"""
Problem 4:
Write a Python program to test whether a number is within 100 of 1000 or 2000.

Example:
within_100_of_1000_or_2000(950) should return True
within_100_of_1000_or_2000(1050) should return True
within_100_of_1000_or_2000(100) should return False
"""


def within_100_of_1000_or_2000(number):
    if (number>900 and number<1100) or (number>1900 and number<2100):
        return True
    else: return False

n = int(input("Enter number: "))
print(within_100_of_1000_or_2000(n))


"""
Problem 5:
Write a Python program to calculate the sum of three given numbers. 
If the values are equal, return three times their sum.

Example:
sum_three_numbers(1, 2, 3) should return 6
sum_three_numbers(3, 3, 3) should return 27
"""


def sum_three_numbers(a, b, c):
    if a != b != c: return a+b+c
    else: return 3*(a+b+c)


a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))
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
    if s.startswith("Is"): return s
    else: return "Is"+s


string = str(input("Enter String: "))
print(new_string_with_is(string))

"""
Problem 7:
Write a Python program that returns a string that is n (non-negative integer) copies of a given string.

Example:
repeat_string("abc", 2) should return "abcabc"
repeat_string("xyz", 3) should return "xyzxyzxyz"
"""


def repeat_string(s, n):
    word=""
    while n!=0:
        word=word+s
        n=n-1
    return word


string = input("Enter String: ")
n = int(input("Enter non-negative integer: "))
print(repeat_string(string, n))
"""
Problem 8:
Write a Python program that determines whether a given number (accepted from the user) is even or odd, 
and prints an appropriate message to the user.

Example:
even_or_odd(10) should return "10 is even"
even_or_odd(3) should return "3 is odd"
"""


def even_or_odd(number):
    if number % 2 == 0: return ("{} is even" .format(number))
    else: return ("{} is odd" .format(number))


n = int(input("Enter number: "))
print(even_or_odd(n))
"""
Problem 9:
Write a Python program to count the number 4 in a given list.

Example:
count_fours([1, 4, 6, 4, 7, 4]) should return 3
"""


def count_fours(lst):
    count=0
    for i in range(0, len(l)):
        if lst[i] == 4: count=count+1
    return count


l=[]
size=int(input("Enter list size: "))
print("Enter list of integers: ")
for i in range(0,size):
    x=int(input())
    l.append(x)
print(count_fours(l))

"""
Problem 10:
Write a Python program to get n (non-negative integer) copies of the first 2 characters of a given string. 
Return n copies of the whole string if the length is less than 2.

Example:
repeat_first_two_chars("abcdef", 3) should return "ababab"
repeat_first_two_chars("a", 3) should return "aaa"
"""


def repeat_first_two_chars(s, n):
    res = ""
    output = ""
    if len(s)>2:
        for i in range(0,2):
            res=res+s[i]
        for i in range(0,n):
            output=output+res
        return output
    else:
        for i in range(0,n):
            output=output+s
        return output


string = str(input("Enter string: "))
n = int(input("Enter number: "))
print(repeat_first_two_chars(string,n))
"""
Problem 11:
Write a Python program to test whether a passed letter is a vowel or not.

Example:
is_vowel("a") should return True
is_vowel("b") should return False
"""


def is_vowel(char):
    if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U' :
        return True
    else: return False

c = str(input("Enter a character: "))
print(is_vowel(c))