#!/usr/bin/env python

"""
A pangram is a sentence that contains all the letters of the English alphabet at least once, for example:
The quick brown fox jumps over the lazy dog.
Your task here is to write a function to check a sentence to see if it is a pangram or not.
"""

import string


def is_pangram(candidate):
    letters = set(string.ascii_lowercase)
    candidate = set(candidate.replace(" ", "").lower())
    return letters == candidate or False


if __name__ == "__main":
    print is_pangram("The quick brown fox jumps over the lazy dog")