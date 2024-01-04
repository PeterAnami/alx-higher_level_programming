#!/usr/bin/python3

"""
This module creates a function add_integer for adding integers

"""


def add_integer(a, b=98):

    """
    adds integers
        Args:
        a: first integer
        b: second integer, defaults to 98 if not given

    """

    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    return int(a) + int(b)
