"""
Problem 95:
Write a Python lambda function that takes two arguments x and y and returns their sum.

Example:
sum_lambda = lambda x, y: ...
"""

sum_lambda = lambda x, y: x + y  # Replace None with your lambda function

"""
Problem 96:
Write a Python function called `multiply` that takes two arguments x and y and returns their product. Use keyword arguments to specify the values of x and y.

Example:
multiply(x=3, y=4) should return 12
"""


def multiply(x, y):
    return x * y


"""
Problem 97:
Write a Python lambda function that takes a list of numbers and returns the list sorted in descending order.

Example:
sort_desc = lambda lst: ...
"""

sort_desc = lambda lst: None  # Replace None with your lambda function

"""
Problem 98:
Write a Python function called `greet` that takes a name and a greeting message as keyword arguments and returns a greeting string.

Example:
greet(name="Alice", message="Hello") should return "Hello, Alice!"
"""


def greet(name, message='Hello'):
    return message + ', ' + name


"""
Problem 99:
Write a Python lambda function that takes a number and returns its square root.

Example:
sqrt_lambda = lambda x: ...
"""

sqrt_lambda = lambda x: x ** 0.5  # Replace None with your lambda function

"""
Problem 100:
Write a Python function called `apply_discount` that takes the original price and a discount percentage as keyword arguments and returns the final price after applying the discount.

Example:
apply_discount(price=100, discount=10) should return 90.0
"""


def apply_discount(price, discount):
    f_p = price - (price * discount/100)
    return f_p


"""
Problem 101:
Write a Python lambda function that takes a string and returns the string in uppercase.

Example:
uppercase_lambda = lambda s: ...
"""

uppercase_lambda = lambda s: s.upper()  # Replace None with your lambda function

"""
Problem 102:
Write a Python function called `power` that takes two arguments, base and exponent, and returns the result of raising the base to the power of the exponent. Use keyword arguments to specify the values.

Example:
power(base=2, exponent=3) should return 8
"""


def power(base, exponent):
    return base ** exponent


"""
Problem 103:
Write a Python lambda function that takes a list of strings and returns a new list with each string reversed.

Example:
reverse_strings_lambda = lambda lst: ...
"""

reverse_strings_lambda = lambda lst: lst[::-1]  # Replace None with your lambda function

"""
Problem 104:
Write a Python function called `create_sentence` that takes a subject, verb, and object as keyword arguments and returns a complete sentence.

Example:
create_sentence(subject="The cat", verb="chased", object="the mouse") should return "The cat chased the mouse."
"""


def create_sentence(subject, verb, object):
    return F'{subject} {verb} {object}'
