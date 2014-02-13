#!/usr/bin/env python

"""
Define a function sum() and a function multiply() that sums and multiplies (respectively) all the numbers in a list of
numbers. For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.
"""


def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total


def multiply(numbers):
    total = 1
    for number in numbers:
        total = total * number
    return total


if __name__ == "__main__":
    print sum([1, 2, 3, 4])
    print multiply([1, 2, 3, 4])

