"""
Problem 69:
Write a Python program that takes a string and an integer n, and returns the string replicated n times.

Example:
replicate_string("Hello", 3) should return "HelloHelloHello"
"""


def replicate_string(s, n):
    replicate_string=s*n
    return replicate_string
#print(replicate_string("Hello",3))


"""
Problem 70:
Write a Python program that takes two strings and returns their concatenation.

Example:
concatenate_strings("Alice", "Bob") should return "AliceBob"
"""


def concatenate_strings(s1, s2):
    concatenate_strings=s1+s2
    return concatenate_strings
#print(concatenate_strings("Alice","Bob"))


"""
Problem 71:
Write a Python program to check if a given string contains a specific substring.

Example:
contains_substring("Hello, world!", "world") should return True
contains_substring("Hello, world!", "Python") should return False
"""


def contains_substring(s, sub):
    if sub in s:
        return True
    else:
        return False
#print(contains_substring("Hello, world!", "world"))


"""
Problem 72:
Write a Python program to convert a string to an integer.

Example:
string_to_int("123") should return 123
"""


def string_to_int(s):
    return int(s)
#print(string_to_int("123"))

"""
Problem 73:
Write a Python program that uses the len() function to return the length of a given list.

Example:
list_length([1, 2, 3, 4, 5]) should return 5
"""


def list_length(lst):
    return len(lst)
#print(list_length([1,2,3,5]))


"""
Problem 74:
Write a Python program that takes a list of integers and returns a new list with each integer incremented by 1 using a for loop.

Example:
increment_list([1, 2, 3]) should return [2, 3, 4]
"""


def increment_list(lst):
    for number in lst:
        num=number+1
    return lst
#print(increment_list([1,2,3]))







"""
Problem 75:
Write a Python program that uses a while loop to print the numbers from 1 to 10.

Example:
print_numbers_while() should print:
1
2
3
4
5
6
7
8
9
10
"""

def print_numbers_while():
    num = 1
    while num<=10:
        return num
        num+=1
print_numbers_while()







"""
Problem 76:
Write a Python program that uses an if statement to check if a number is even or odd.

Example:
is_even_or_odd(4) should return "Even"
is_even_or_odd(7) should return "Odd"
"""


def is_even_or_odd(n):
    if n%2==0:
        return "Even"
    else:
        return "Odd"
#print(is_even_or_odd(7))



"""
Problem 77:
Write a Python program that uses a for loop and the range() function to print all even numbers between 1 and 20.

Example:
print_even_numbers() should print:
2
4
6
8
10
12
14
16
18
20
"""


def print_even_numbers():
    num=range(1,21)
    for n in num:
        if n%2==0:
            return n
print_even_numbers()







"""
Problem 78:
Write a Python program that uses a ternary conditional operator to return "Positive" if a number is positive, and "Non-positive" otherwise.

Example:
check_positive(-5) should return "Non-positive"
check_positive(10) should return "Positive"
"""


def check_positive(n):
    a=f'Positive' if n==abs(n) else 'Non-positive'
    return a
#print(check_positive(5))
#print(check_positive(5))


"""
Problem 79:
Write a Python program that simulates a basic switch-case statement using if-elif-else to match single values.

Example:
basic_switch_case(1) should return "One"
basic_switch_case(2) should return "Two"
basic_switch_case(3) should return "Three"
"""


def basic_switch_case(value):
    if value==1:
        return "One"
    elif value==2:
        return "Two"
    else:
        return "Three"

#print(basic_switch_case(2))

"""
Problem 80:
Write a Python program that uses the continue statement to skip printing the number 5 in a loop from 1 to 10.

Example:
skip_number_five() should print:
1
2
3
4
6
7
8
9
10
"""


def skip_number_five():
    num=0
    while num<=9:
        num+=1
        if num==5:
            continue
        return num
skip_number_five()



"""
Problem 81:
Write a Python program that uses the break statement to exit a loop when the number 5 is encountered in a loop from 1 to 10.

Example:
break_at_five() should print:
1
2
3
4
"""


def break_at_five():
    num=0
    while num<=10:
        num+=1
        if num==5:
            break
        return num
break_at_five()



"""
Problem 82:
Write a Python program that uses a for-else statement to search for an element in a list. If the element is found, return "Found", otherwise return "Not found".

Example:
search_list([1, 2, 3, 4, 5], 3) should return "Found"
search_list([1, 2, 3, 4, 5], 6) should return "Not found"
"""


def search_list(lst, target):
    for target in lst[0:len(lst)]:
        return "Found"
    else:
        return "Not Found"
#print(search_list([1,2,3,4,5],8))




"""
Problem 83:
Write a Python program that uses sys.exit() to end a program when a specific condition is met.

Example:
end_program_if_negative(-1) should exit the program
"""

import sys


def end_program_if_negative(n):
    if n==abs(n):
        return n
    else:
        sys.exit()
#print(end_program_if_negative(5))