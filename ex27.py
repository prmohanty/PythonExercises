#!/usr/bin/env python

"""
Write a program that maps a list of words into a list of integers representing the lengths of the corresponding words.
Write it in three different ways: 1) using a for-loop, 2) using the higher order function map(), and 3) using list
comprehensions.
"""


def map_to_lengths_for(words):
    lengths = []
    for word in words:
        lengths.append(len(word))
    return lengths


def map_to_lengths_map(words):
    return map(len, words)


def map_to_lengths_lists(words):
    return [len(word) for word in words]


if __name__ == "__main__":
    words = ['abv', 'try me', 'test']
    print map_to_lengths_for(words)
    print map_to_lengths_map(words)
    print map_to_lengths_lists(words)