#!/usr/bin/env python

"""
Write a program that maps a list of words into a list of integers representing the lengths of the corresponding words.
"""


def map_list_to_len(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths


if __name__ == "__main__":
    words = ['test', 'abc', 'biggest one']
    print map_list_to_len(words)
