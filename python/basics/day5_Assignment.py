"""
Problem 84:
Write a Python function called `square` that takes a number as an argument and returns its square.

Example:
square(4) should return 16
"""


def square(x):
    return x**2
    pass


"""
Problem 85:
Write a Python function called `is_palindrome` that takes a string as an argument and returns True if the string is a palindrome, and False otherwise.

Example:
is_palindrome("madonna") should return False
is_palindrome("madam") should return True
"""


def is_palindrome(s):

    if s[::-1] == s:
        return True
    else:
        return False
    pass


"""
Problem 86:
Write a Python function called `factorial` that takes a non-negative integer as an argument and returns the factorial of that number.

Example:
factorial(5) should return 120
"""


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact
    pass


"""
Problem 87:
Write a Python function called `fibonacci` that takes an integer n as an argument and returns the nth Fibonacci number.

Example:
fibonacci(7) should return 13
"""


def fibonacci(n):
    a = 0
    b = 1
    for i in range(1, n):
        c = a + b
        a = b
        b = c
    return b
    pass


"""
Problem 88:
Write a Python function called `is_even` that takes a number as an argument and returns True if the number is even, and False otherwise.

Example:
is_even(4) should return True
is_even(7) should return False
"""


def is_even(n):
    if n%2==0:
        return True
    else:
        return False
    pass


"""
Problem 89:
Write a Python lambda function that takes two numbers and returns their product.

Example:
product = lambda a, b: a * b
product(3, 4) should return 12
"""

product = lambda a, b: a*b  # Replace None with your lambda function


"""
Problem 90:
Write a Python function called `apply_function` that takes a function and a value as arguments and returns the result of applying the function to the value.

Example:
def increment(x):
    return x + 1

apply_function(increment, 5) should return 6
"""


def increment(x):
    return x + 1
def apply_function(increment, value):
    return increment(value)



"""
Problem 91:
Write a Python function called `filter_even_numbers` that takes a list of numbers and returns a new list with only the even numbers.

Example:
filter_even_numbers([1, 2, 3, 4, 5]) should return [2, 4]
"""


def filter_even_numbers(lst):
    newlst = []
    for i in lst:
        if i % 2 == 0:
            newlst.append(i)
    return newlst
    pass


"""
Problem 92:
Write a Python lambda function that takes a number and returns True if the number is greater than 10, and False otherwise.

Example:
greater_than_ten = lambda x: x > 10
greater_than_ten(15) should return True
greater_than_ten(5) should return False
"""

greater_than_ten = lambda x: x>10  # Replace None with your lambda function

"""
Problem 93:
Write a Python function called `sort_list` that takes a list of numbers and returns the list sorted in ascending order using a lambda function.

Example:
sort_list([3, 1, 4, 1, 5, 9]) should return [1, 1, 3, 4, 5, 9]
"""


def sort_list(lst):
    return fun(lst)
fun = lambda lst: sorted(lst)



"""
Problem 94:
Write a Python function called `apply_lambda` that takes a lambda function and a list of numbers, and returns a new list with the lambda function applied to each number.

Example:
apply_lambda(lambda x: x * 2, [1, 2, 3]) should return [2, 4, 6]
"""


def apply_lambda(func, lst):
    newlist = []
    for i in lst:
        newlist.append(func(i))
    return newlist
func = lambda x: x * 2
