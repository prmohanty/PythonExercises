#!/usr/bin/env python

"""
Using the higher order function filter(), define a function filter_long_words() that takes a list of words and an
integer n and returns the list of words that are longer than n.
"""


def filter_long_words(words, n):
    return filter(lambda x: len(x) > n, words)


print filter_long_words(['test', 'not', 'this should'], 5)