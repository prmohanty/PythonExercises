#!/usr/bin/env python

"""
Write a version of a palindrome recognizer that also accepts phrase palindromes such as "Go hang a salami I'm a lasagna
hog.", "Was it a rat I saw?", "Step on no pets", "Sit on a potato pan, Otis", "Lisa Bonet ate no basil", "Satan,
oscillate my metallic sonatas", "I roamed under it as a tired nude Maori", "Rise to vote sir", or the exclamation
"Dammit, I'm mad!". Note that punctuation, capitalization, and spacing are usually ignored.
"""

import string
from ex8 import is_palindrome


def is_palindrome_extended(candidate):
    candidate = ''.join([word for word in candidate.lower().split()])
    candidate = ''.join([char for char in candidate if char not in string.punctuation])
    return is_palindrome(candidate)


if __name__ == "__main__":
    print is_palindrome_extended("Rise to vote sir")