# test_assignment.py

# Importing functions from the assignment file
from python.basics.day4_Assignment import replicate_string, concatenate_strings, contains_substring, string_to_int, \
    list_length, increment_list, print_numbers_while, is_even_or_odd, print_even_numbers, check_positive, \
    basic_switch_case, skip_number_five, break_at_five, search_list, end_program_if_negative


# Test cases for replicate_string function
def test_replicate_string():
    assert replicate_string("Hello", 3) == "HelloHelloHello"
    assert replicate_string("Alice", 2) == "AliceAlice"
    assert replicate_string("Bob", 1) == "Bob"
    # Add more test cases as needed


# Test cases for concatenate_strings function
def test_concatenate_strings():
    assert concatenate_strings("Alice", "Bob") == "AliceBob"
    assert concatenate_strings("Hello", "World") == "HelloWorld"
    assert concatenate_strings("", "Test") == "Test"
    # Add more test cases as needed


# Test cases for contains_substring function
def test_contains_substring():
    assert contains_substring("Hello, world!", "world") == True
    assert contains_substring("Hello, world!", "Python") == False
    assert contains_substring("OpenAI", "AI") == True
    # Add more test cases as needed


# Test cases for string_to_int function
def test_string_to_int():
    assert string_to_int("123") == 123
    assert string_to_int("0") == 0
    assert string_to_int("-456") == -456
    # Add more test cases as needed


# Test cases for list_length function
def test_list_length():
    assert list_length([1, 2, 3, 4, 5]) == 5
    assert list_length([]) == 0
    assert list_length([1]) == 1
    # Add more test cases as needed


# Test cases for increment_list function
def test_increment_list():
    assert increment_list([1, 2, 3]) == [2, 3, 4]
    assert increment_list([0, -1, -2]) == [1, 0, -1]
    assert increment_list([]) == []
    # Add more test cases as needed


# Test cases for print_numbers_while function
def test_print_numbers_while(capsys):
    print_numbers_while()
    captured = capsys.readouterr()
    assert captured.out == "1\n2\n3\n4\n5\n6\n7\n8\n9\n10\n"
    # Add more test cases as needed


# Test cases for is_even_or_odd function
def test_is_even_or_odd():
    assert is_even_or_odd(4) == "Even"
    assert is_even_or_odd(7) == "Odd"
    assert is_even_or_odd(0) == "Even"
    # Add more test cases as needed


# Test cases for print_even_numbers function
def test_print_even_numbers(capsys):
    print_even_numbers()
    captured = capsys.readouterr()
    assert captured.out == "2\n4\n6\n8\n10\n12\n14\n16\n18\n20\n"
    # Add more test cases as needed


# Test cases for check_positive function
def test_check_positive():
    assert check_positive(-5) == "Non-positive"
    assert check_positive(10) == "Positive"
    assert check_positive(0) == "Non-positive"
    # Add more test cases as needed


# Test cases for basic_switch_case function
def test_basic_switch_case():
    assert basic_switch_case(1) == "One"
    assert basic_switch_case(2) == "Two"
    assert basic_switch_case(3) == "Three"
    assert basic_switch_case(4) == "Unknown"
    # Add more test cases as needed


# Test cases for skip_number_five function
def test_skip_number_five(capsys):
    skip_number_five()
    captured = capsys.readouterr()
    assert captured.out == "1\n2\n3\n4\n6\n7\n8\n9\n10\n"
    # Add more test cases as needed


# Test cases for break_at_five function
def test_break_at_five(capsys):
    break_at_five()
    captured = capsys.readouterr()
    assert captured.out == "1\n2\n3\n4\n"
    # Add more test cases as needed


# Test cases for search_list function
def test_search_list():
    assert search_list([1, 2, 3, 4, 5], 3) == "Found"
    assert search_list([1, 2, 3, 4, 5], 6) == "Not found"
    assert search_list([], 1) == "Not found"
    # Add more test cases as needed


# Test cases for end_program_if_negative function
def test_end_program_if_negative():
    # This is tricky to test as it exits the program
    # One way is to mock sys.exit() in tests
    import pytest
    with pytest.raises(SystemExit):
        end_program_if_negative(-1)
    # Add more test cases as needed
