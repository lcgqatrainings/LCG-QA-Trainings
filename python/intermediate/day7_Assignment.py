"""
Problem 105:
Write a Python function called `flatten_list` that takes a nested list and returns a flattened version of the list using a recursive approach.

Example:
flatten_list([1, [2, 3], [4, [5, 6]]]) should return [1, 2, 3, 4, 5, 6]
"""


def flatten_list(nested_list):
    newlst=[]
    for row in nested_list:
        for i in row:
            newlst.append(i)
    print(newlst)
    pass


"""
Problem 106:
Write a Python function called `unique_elements` that takes a list and returns a list of unique elements, maintaining their original order.

Example:
unique_elements([1, 2, 2, 3, 4, 4, 5]) should return [1, 2, 3, 4, 5]
"""


def unique_elements(lst):
    nlst = []
    for i in lst:
        if i not in nlst:
            nlst.append(i)
    print(nlst)
    pass


"""
Problem 107:
Write a Python lambda function that takes a dictionary of student names and their scores, and returns a dictionary with student names as keys and their grades ('A', 'B', 'C', 'D', 'F') as values based on the scores.

Example:
grade_students = lambda scores: ...
grades = grade_students({'Alice': 85, 'Bob': 72, 'Charlie': 90})
"""

grade_students = lambda scores: [print("A")if i>=86 and i<=90 else print("B") if i>=75 and i<=85 else print("C") for i in scores.values()]  # Replace None with your lambda function

"""
Problem 108:
Write a Python function called `transpose_matrix` that takes a 2D list (matrix) and returns its transpose.

Example:
transpose_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) should return [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
"""


def transpose_matrix(matrix):
    m = 3
    for i in range(m):
        for j in range(i + 1, m):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    return matrix
    pass


"""
Problem 109:
Write a Python function called `most_common_words` that takes a list of strings and returns a dictionary with the most common word in each string as keys and their frequencies as values.

Example:
most_common_words(["the cat in the hat", "the quick brown fox", "the fox jumps over the lazy dog"]) should return {'the': 3, 'fox': 2}
"""


def most_common_words(strings):
    count = 0
    count_fox = 0
    for i in strings:
        if "the" in i.split():
            count = count + 1
        if "fox" in i.split():
            count_fox = count_fox + 1
    print(count, count_fox)
    pass


"""
Problem 110:
Write a Python lambda function that takes a list of tuples, each containing a name and age, and returns a list of names sorted by age.

Example:
sort_by_age = lambda data: ...
sorted_names = sort_by_age([("Alice", 25), ("Bob", 20), ("Charlie", 23)])
"""

sort_by_age = lambda data: sorted(data,key=lambda val:val[1])  # Replace None with your lambda function

"""
Problem 111:
Write a Python function called `filter_dict` that takes a dictionary and a predicate function, and returns a new dictionary containing only the items that satisfy the predicate.

Example:
filter_dict({'a': 1, 'b': 2, 'c': 3}, lambda k, v: v > 1) should return {'b': 2, 'c': 3}
"""


def filter_dict(d, predicate):
    ndic = {}
    for k, v in d.items():
        if predicate(k, v):
            ndic[k] = v
    print(ndic)
    pass


"""
Problem 112:
Write a Python function called `merge_dictionaries` that takes a list of dictionaries and returns a single dictionary by merging them. In case of conflicts, the value from the last dictionary in the list should be used.

Example:
merge_dictionaries([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]) should return {'a': 1, 'b': 3, 'c': 4}
"""


def merge_dictionaries(dicts):
    ndict = {}
    for i in dicts:
        ndict.update(i)
    print(ndict)
    pass


"""
Problem 113:
Write a Python function called `nested_sum` that takes a list of lists of integers and returns the sum of all integers.

Example:
nested_sum([[1, 2, 3], [4, 5], [6]]) should return 21
"""


def nested_sum(lst):
    sum = 0
    for i in lst:
        for j in i:
            sum = sum + j
    print(sum)
    pass


"""
Problem 114:
Write a Python lambda function that takes a list of numbers and returns a list of their squares, but only for numbers greater than 10.

Example:
filter_and_square = lambda lst: ...
result = filter_and_square([5, 12, 9, 20])
"""

filter_and_square = lambda lst: list(filter(lambda i: i is not None,[i*i if(i*i)>10 else None for i in lst]))  # Replace None with your lambda function
