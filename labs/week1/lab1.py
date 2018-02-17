"""
Jon Shallow
UNHM COMP705/805 Lab 1
An Introduction to Python
Jan 19, 2018

The purpose of this file is to learn BASIC python syntax and data structures.
There is an accompanying test file. Place both files in the same directory,
and then run:
$ python tests.py

You will see a print out of tests that are being run, and your result.
Please see: https://www.python.org/dev/peps/pep-0008/ for style guidelines
"""

def give_me_a_string():
    """
    This function returns a string value
    """
    my_string = 'good morning'
    my_string = my_string.upper()
    return my_string

def give_me_an_integer():
    """
    This function returns an integer value
    """
    my_int = 7
    my_int = my_int*5 - 10
    return my_int

def give_me_a_boolean():
    """
    This function returns a boolean value
    """
    r = range(10)
    result = 10 in r
    return result

def give_me_a_float():
    """
    This function returns a float value
    """
    from math import pi
    r = 3.5
    area = (pi * r**2)
    return area

def give_me_a_list():
    """
    This function returns a list
    """
    my_list = ['pink', '3', 'candy', 'g00d']
    result = []
    for item in my_list:
        if item.isalpha( ):
            result.append(item)
    return result

def give_me_a_dictionary():
    """
    This function returns a dictionary
    """
    color_list = ['yellow', 'green', 'green', 'orange', 'green']
    dict = {'red':10, 'blue':4, 'green':2}
    for color in color_list:
        if color in dict:
            dict[color] = dict[color] + 1
        else:
            dict[color] = 1
    return dict

def give_me_a_tuple():
    """
    This function returns a tuple
    """
    tpl = ('n', 0, 'changes', 2, 'tuples')
    return tpl[0:3]

def sum_numbers_one_to_ten():
    """
    This function returns the sum of all numbers one to ten
    Use the range function:
    https://docs.python.org/3/library/functions.html
    Use the accumulator pattern:
    http://interactivepython.org/runestone/static/thinkcspy/Functions/TheAccumulatorPattern.html
    """
    theSum = 0
    for num in range(1, 11):
        theSum = theSum + num
    return theSum

def check_is_even(number):
    """
    This function returns True if number is even
    else False
    hint: use modulo operator
    https://docs.python.org/3/reference/expressions.html
    """
    if number % 2 == 0:
        return True
    else:
        return False

def check_is_less_than(number1, number2):
    """
    This functions returns True if number1 < number2
    else False
    """
    if number1 < number2:
        return True
    else:
        return False

def is_between(x, y, z):
    """
    x, y, z: Numbers
    Decides if the 2nd number is between the 1st and 3rd.
    Returns: True if x <= y <= z, False otherwise
    """
    if (x <= y) and (y <= z):
        return True
    else:
        return False

def sum_odd_to(n):
    """
    Calculates the sum of all odd positive integers from 1 to number. 
    including number. 

    Uses the accumulator pattern.

    n: Non-negative integer.
    Returns: the sum of all odd positive numbers from 1 to n.
    """
    if n >= 1:
        theSum = 0
        for num in range(1, n + 1, 2):
            theSum = theSum + num
        return theSum
    else:
        print("The value entered is not a positive integer >= 1.")