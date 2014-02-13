#!/usr/bin/env python

"""
Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are
longer than n.
"""


def filter_long_words(words, n):
    return [word for word in words if len(word) > n]


if __name__ == "__main__":
    print filter_long_words(['a', 'avg', 'abcde', 'zxcw', 'b'], 3)