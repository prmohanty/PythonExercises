#!/usr/bin/env python

"""
Define a function reverse() that computes the reversal of a string.
For example, reverse("I am testing") should return the string "gnitset ma I".
"""


def reverse(string):
    result = []
    for word in string.split()[::-1]:
        result.append(word[::-1])
    return " ".join(result)


print reverse("I am testing")