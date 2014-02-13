#!/usr/bin/env python

"""
Write a function find_longest_word() that takes a list of words and returns the length of the longest one.
"""

from ex14 import map_list_to_len


def find_longest_word(words):
    return max(map_list_to_len(words))


if __name__ == "__main__":
    print find_longest_word(['a', 'abc', 'longest'])