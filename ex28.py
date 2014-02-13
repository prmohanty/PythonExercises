#!/usr/bin/env python

"""
Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
Use only higher order functions.
"""


def find_longest_word(words):
    return max(map(len, words))


if __name__ == "__main__":
    print find_longest_word(['small', 'biggest', 'a huge one here'])