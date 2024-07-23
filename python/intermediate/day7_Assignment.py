"""
Problem 105:
Write a Python function called `flatten_list` that takes a nested list and returns a flattened version of the list using a recursive approach.

Example:
flatten_list([1, [2, 3], [4, [5, 6]]]) should return [1, 2, 3, 4, 5, 6]
"""


def flatten_list(nested_list):
    f_lst = []
    # for i in range(len(nested_list)):
    #     if isinstance(nested_list[i], list):
    #         for j in range(len(nested_list[i])):
    #             if isinstance(nested_list[i][j],list):
    #                 for k in range(len(nested_list[i][j])):
    #                     f_lst.append(nested_list[i][j][k])
    #             else:
    #                 f_lst.append(nested_list[i][j])
    #     else:
    #         f_lst.append(nested_list[i])
    for item in nested_list:
        if isinstance(item, list):
            f_lst.extend(flatten_list(item))
        else:
            f_lst.append(item)
    return f_lst


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
        for j in range(i + 1, len(lst) - 1):
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
# grades = lambda scores: ('A' if scores >= 90 else
#                          'B' if scores >= 80 else
#                          'c' if scores >= 70 else
#                          'D' if scores >= 60 else
#                          'E')

grade_students = lambda scores: {name: ('A' if scores >= 90 else
                                        'B' if scores >= 80 else
                                        'c' if scores >= 70 else
                                        'D' if scores >= 60 else
                                        'E') for name, scores in scores.items()}  # Replace None with your lambda function

"""
Problem 108:
Write a Python function called `transpose_matrix` that takes a 2D list (matrix) and returns its transpose.

Example:
transpose_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) should return [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
"""


def transpose_matrix(matrix):
    # ([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]
    # s = []
    # s.append([matrix[0][0], matrix[1][0], matrix[2][0]])
    # s.append([matrix[0][1], matrix[1][1], matrix[2][1]])
    # s.append([matrix[0][2], matrix[1][2], matrix[2][2]])
    if len(matrix[0]) == 0:
        return matrix
    k = []
    for c in range(0, len(matrix[0])):
        r1 = []
        for j in range(0, len(matrix)):
            r1.append(matrix[j][c])
        k.append(r1)
    return k


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

sort_by_age = lambda data: list(map(lambda x: x[0], sorted(data, key=lambda x: x[1])))  # Replace None with your lambda function

# sort_by_age2 = lambda data: [name for name,age in sorted(data, key=lambda x : x[1])]


"""
Problem 111:
Write a Python function called `filter_dict` that takes a dictionary and a predicate function, and returns a new dictionary containing only the items that satisfy the predicate.

Example:
filter_dict({'a': 1, 'b': 2, 'c': 3}, lambda k, v: v > 1) should return {'b': 2, 'c': 3}
"""

predicate = lambda key, value: value > 1


def filter_dict(d, predicate):
    filtered_d = {}
    for key, value in d.items():
        if predicate(key, value):
            filtered_d[key] = value
    # return {key: value for key, value in d.items() if predicate(key, value)}
    return filtered_d


"""
Problem 112:
Write a Python function called `merge_dictionaries` that takes a list of dictionaries and returns a single dictionary by merging them. In case of conflicts, the value from the last dictionary in the list should be used.

Example:
merge_dictionaries([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]) should return {'a': 1, 'b': 3, 'c': 4}
"""


def merge_dictionaries(dicts):
    c = {}
    for d in dicts:
        c.update(d)
    return c


"""
Problem 113:
Write a Python function called `nested_sum` that takes a list of lists of integers and returns the sum of all integers.

Example:
nested_sum([[1, 2, 3], [4, 5], [6]]) should return 21
"""


def nested_sum(lst):
    sum_ = 0
    for i in range(0, len(lst)):
        for j in lst[i]:
            sum_ += j
    return sum_


"""
Problem 114:
Write a Python lambda function that takes a list of numbers and returns a list of their squares, but only for numbers greater than 10.

Example:
filter_and_square = lambda lst: ...
result = filter_and_square([5, 12, 9, 20])
"""

filter_and_square = lambda lst: list(map(lambda x: x**2, filter(lambda x: x > 10, lst)))
# Replace None with your lambda function
