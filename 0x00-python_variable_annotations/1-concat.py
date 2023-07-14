#!/usr/bin/env python3
"""Write a type-annotated function concat that takes a string str1
and a string str2 as arguments and returns a concatenated string.
"""
from math import floor as roundup


def floor(n: float) -> int:
    """Rounds up a float
    Keyword arguments:
    n -- float variable
    Return: floor of the float, n
    """
    return roundup(n)