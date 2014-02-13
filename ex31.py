#!/usr/bin/env python

"""
Implement the higher order functions map(), filter() and reduce().
(They are built-in but writing them yourself may be a good exercise.)
"""


def map(function, iterable):
    results = []
    for i in iterable:
        results.append(function(i))
    return results


def filter(function, iterable):
    return [i for i in iterable if function(i) == True]


def reduce(function, iterable):
    #TODO: http://docs.python.org/2/library/functions.html#reduce
    pass


if __name__ == "__main__":
    pass