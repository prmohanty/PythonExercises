#!/usr/bin/env python

"""
Define a procedure histogram() that takes a list of integers and prints a histogram to the screen.
For example, histogram([4, 9, 7]) should print the following:
****
*********
*******
"""

from ex11 import generate_n_chars


def histogram(li):
    for n in li:
        print generate_n_chars(n, '*')


if __name__ == "__main__":
    histogram([4, 9, 7])