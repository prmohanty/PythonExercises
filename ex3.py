#!/usr/bin/env python

"""
Define a function that computes the length of a given list or string.
(It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)
"""


def length(string):
    count = 0
    for i in string:
        count += 1
    return count


if __name__ == "__main__":
    print length("test string")