"""
Problem 95:
Write a Python lambda function that takes two arguments x and y and returns their sum.

Example:
sum_lambda = lambda x, y: ...
"""
import math

sum_lambda = lambda x, y: x+y  # Replace None with your lambda function
sum_lambda(4, 5)
"""
Problem 96:
Write a Python function called `multiply` that takes two arguments x and y and returns their product. Use keyword arguments to specify the values of x and y.

Example:
multiply(x=3, y=4) should return 12
"""


def multiply(x, y):
   z=x*y
   return z
multiply(x=3,y=4)


"""
Problem 97:
Write a Python lambda function that takes a list of numbers and returns the list sorted in descending order.

Example:
sort_desc = lambda lst: ...
"""

sort_desc = lambda lst: sorted(lst, reverse=True)  # Replace None with your lambda function
sort_desc([5,10,-3,0,11])

"""
Problem 98:
Write a Python function called `greet` that takes a name and a greeting message as keyword arguments and returns a greeting string.

Example:
greet(name="Alice", message="Hello") should return "Hello, Alice!"
"""


def greet(name, message):
    return f"{message},{name}!"
greet(name="Alice",message="Hello")


"""
Problem 99:
Write a Python lambda function that takes a number and returns its square root.

Example:
sqrt_lambda = lambda x: ...
"""
import math
sqrt_lambda = lambda x: math.sqrt(x)  # Replace None with your lambda function
sqrt_lambda(25)

"""
Problem 100:
Write a Python function called `apply_discount` that takes the original price and a discount percentage as keyword arguments and returns the final price after applying the discount.

Example:
apply_discount(price=100, discount=10) should return 90.0
"""


def apply_discount(price, discount):
    final_price=price-discount
    return float(final_price)
apply_discount(price=100,discount=10)


"""
Problem 101:
Write a Python lambda function that takes a string and returns the string in uppercase.

Example:
uppercase_lambda = lambda s: ...
"""

uppercase_lambda = lambda s: s.upper()  # Replace None with your lambda function
uppercase_lambda("1234ab")

"""
Problem 102:
Write a Python function called `power` that takes two arguments, base and exponent, and returns the result of raising the base to the power of the exponent. Use keyword arguments to specify the values.

Example:
power(base=2, exponent=3) should return 8
"""


def power(base, exponent):
    power=base**exponent
    return power
power(base=2,exponent=3)


"""
Problem 103:
Write a Python lambda function that takes a list of strings and returns a new list with each string reversed.

Example:
reverse_strings_lambda = lambda lst: ...
"""

reverse_strings_lambda = lambda lst: lst[::-1]# Replace None with your lambda function

reverse_strings_lambda(["MOON","AYAAN"])

"""
Problem 104:
Write a Python function called `create_sentence` that takes a subject, verb, and object as keyword arguments and returns a complete sentence.

Example:
create_sentence(subject="The cat", verb="chased", object="the mouse") should return "The cat chased the mouse."
"""


def create_sentence(subject, verb, object):
    return f"{subject} {verb} {object}."
create_sentence(subject="The cat",verb="chased",object="the mouse")
