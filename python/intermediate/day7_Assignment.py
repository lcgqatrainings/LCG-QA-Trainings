"""
Problem 105:
Write a Python function called `flatten_list` that takes a nested list and returns a flattened version of the list using a recursive approach.

Example:
flatten_list([1, [2, 3], [4, [5, 6]]]) should return [1, 2, 3, 4, 5, 6]
"""


def flatten_list(nested_list):
    pass


"""
Problem 106:
Write a Python function called `unique_elements` that takes a list and returns a list of unique elements, maintaining their original order.

Example:
unique_elements([1, 2, 2, 3, 4, 4, 5]) should return [1, 2, 3, 4, 5]
"""


def unique_elements(lst):
    for i in range(len(lst)):
        if i == len(lst) - 1:
            break
        for j in range(i+1, len(lst)-1):
            if lst[i] == lst[j]:
                lst.pop(j)
    return lst


"""
Problem 107:
Write a Python lambda function that takes a dictionary of student names and their scores, and returns a dictionary with student names as keys and their grades ('A', 'B', 'C', 'D', 'F') as values based on the scores.

Example:
grade_students = lambda scores: ...
grades = grade_students({'Alice': 85, 'Bob': 72, 'Charlie': 90})
"""

grade_students = lambda scores: None  # Replace None with your lambda function

"""
Problem 108:
Write a Python function called `transpose_matrix` that takes a 2D list (matrix) and returns its transpose.

Example:
transpose_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) should return [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
"""


def transpose_matrix(matrix):
    # Your code here
    pass


"""
Problem 109:
Write a Python function called `most_common_words` that takes a list of strings and returns a dictionary with the most common word in each string as keys and their frequencies as values.

Example:
most_common_words(["the cat in the hat", "the quick brown fox", "the fox jumps over the lazy dog"]) should return {'the': 3, 'fox': 2}
"""


def most_common_words(strings):
    # Your code here
    pass


"""
Problem 110:
Write a Python lambda function that takes a list of tuples, each containing a name and age, and returns a list of names sorted by age.

Example:
sort_by_age = lambda data: ...
sorted_names = sort_by_age([("Alice", 25), ("Bob", 20), ("Charlie", 23)])
"""

sort_by_age = lambda data: None  # Replace None with your lambda function

"""
Problem 111:
Write a Python function called `filter_dict` that takes a dictionary and a predicate function, and returns a new dictionary containing only the items that satisfy the predicate.

Example:
filter_dict({'a': 1, 'b': 2, 'c': 3}, lambda k, v: v > 1) should return {'b': 2, 'c': 3}
"""


def filter_dict(d, predicate):
    # Your code here
    pass


"""
Problem 112:
Write a Python function called `merge_dictionaries` that takes a list of dictionaries and returns a single dictionary by merging them. In case of conflicts, the value from the last dictionary in the list should be used.

Example:
merge_dictionaries([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]) should return {'a': 1, 'b': 3, 'c': 4}
"""


def merge_dictionaries(dicts):
    # Your code here
    pass


"""
Problem 113:
Write a Python function called `nested_sum` that takes a list of lists of integers and returns the sum of all integers.

Example:
nested_sum([[1, 2, 3], [4, 5], [6]]) should return 21
"""


def nested_sum(lst):
    # Your code here
    pass


"""
Problem 114:
Write a Python lambda function that takes a list of numbers and returns a list of their squares, but only for numbers greater than 10.

Example:
filter_and_square = lambda lst: ...
result = filter_and_square([5, 12, 9, 20])
"""

filter_and_square = lambda lst: None  # Replace None with your lambda function
