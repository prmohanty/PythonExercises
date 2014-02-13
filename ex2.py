#!/usr/bin/env python

"""
Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.
"""

from ex1 import max


def max_of_three(a, b, c):
    max_temp = max(a, b)
    return max(max_temp, c)


if __name__ == "__main__":
    print max_of_three(1, 2, 3)