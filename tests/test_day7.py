# test_assignment.py

# Importing functions from the assignment file
from python.intermediate.day7_Assignment import flatten_list, unique_elements, grade_students, transpose_matrix, \
    most_common_words, sort_by_age, filter_dict, merge_dictionaries, nested_sum, filter_and_square


# Test cases for flatten_list function
def test_flatten_list():
    assert flatten_list([1, [2, 3], [4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]
    assert flatten_list([]) == []
    assert flatten_list([1, 2, 3]) == [1, 2, 3]
    # Add more test cases as needed


# Test cases for unique_elements function
def test_unique_elements():
    assert unique_elements([1, 2, 2, 3, 4, 4, 5]) == [1, 2, 3, 4, 5]
    assert unique_elements([]) == []
    assert unique_elements([1, 1, 1, 1]) == [1]
    # Add more test cases as needed


# Test cases for grade_students lambda function
def test_grade_students():
    assert grade_students({'Alice': 85, 'Bob': 72, 'Charlie': 90}) == {'Alice': 'B', 'Bob': 'C', 'Charlie': 'A'}
    assert grade_students({}) == {}
    assert grade_students({'Dave': 60}) == {'Dave': 'D'}
    # Add more test cases as needed


# Test cases for transpose_matrix function
def test_transpose_matrix():
    assert transpose_matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]]) == [[1, 4, 7], [2, 5, 8], [3, 6, 9]]
    assert transpose_matrix([[1, 2], [3, 4], [5, 6]]) == [[1, 3, 5], [2, 4, 6]]
    assert transpose_matrix([[]]) == [[]]
    # Add more test cases as needed


# Test cases for most_common_words function
def test_most_common_words():
    assert most_common_words(["the cat in the hat", "the quick brown fox", "the fox jumps over the lazy dog"]) == {
        'the': 3, 'fox': 2}
    assert most_common_words([]) == {}
    assert most_common_words(["hello world", "hello", "world hello"]) == {'hello': 3, 'world': 2}
    # Add more test cases as needed


# Test cases for sort_by_age lambda function
def test_sort_by_age():
    assert sort_by_age([("Alice", 25), ("Bob", 20), ("Charlie", 23)]) == ["Bob", "Charlie", "Alice"]
    assert sort_by_age([]) == []
    assert sort_by_age([("Alice", 25)]) == ["Alice"]
    # Add more test cases as needed


# Test cases for filter_dict function
def test_filter_dict():
    assert filter_dict({'a': 1, 'b': 2, 'c': 3}, lambda k, v: v > 1) == {'b': 2, 'c': 3}
    assert filter_dict({}, lambda k, v: v > 1) == {}
    assert filter_dict({'a': 1}, lambda k, v: v > 1) == {}
    # Add more test cases as needed


# Test cases for merge_dictionaries function
def test_merge_dictionaries():
    assert merge_dictionaries([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}]) == {'a': 1, 'b': 3, 'c': 4}
    assert merge_dictionaries([]) == {}
    assert merge_dictionaries([{'a': 1}, {'a': 2}]) == {'a': 2}
    # Add more test cases as needed


# Test cases for nested_sum function
def test_nested_sum():
    assert nested_sum([[1, 2, 3], [4, 5], [6]]) == 21
    assert nested_sum([[]]) == 0
    assert nested_sum([[-1, -2, -3], [-4, -5], [-6]]) == -21
    # Add more test cases as needed


# Test cases for filter_and_square lambda function
def test_filter_and_square():
    assert filter_and_square([5, 12, 9, 20]) == [144, 400]
    assert filter_and_square([]) == []
    assert filter_and_square([10, 11]) == [121]
    # Add more test cases as needed
