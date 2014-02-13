#!/usr/bin/env python

"""
Using the higher order function reduce(), write a function max_in_list() that takes a list of numbers and returns the
largest one. Then ask yourself: why define and call a new function, when I can just as well call the reduce() function
directly?
"""

from ex1 import max


def max_in_list(numbers):
    return reduce(max, numbers)


if __name__ == "__main__":
    print max_in_list([1, 3, 5, 10, 1, 25])