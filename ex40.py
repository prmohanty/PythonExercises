#!/usr/bin/env python

"""
An anagram is a type of word play, the result of rearranging the letters of a word or phrase to produce a new word or
phrase, using all the original letters exactly once; e.g., orchestra = carthorse, A decimal point = I'm a dot in place.
Write a Python program that, when started 1) randomly picks a word w from given list of words, 2) randomly permutes w
(thus creating an anagram of w), 3) presents the anagram to the user, and 4) enters an interactive loop in which the
user is invited to guess the original word. It may be a good idea to work with (say) colour words only.
The interaction with the program may look like so:

import anagram
Colour word anagram: onwbr
Guess the colour word!
black
Guess the colour word!
brown
Correct!
"""

import random
import itertools

words = ['red', 'black', 'brown', 'green']
word, anagram = random.sample(words, 1)[0], ''

perms = itertools.permutations(word)
for perm in perms:
    if ''.join(perm) != word:
        anagram = ''.join(perm)
        break

print "Colour word anagram: %s" % anagram
input = raw_input("Guess the colour word!\n")

while input != word:
    input = raw_input("Guess the colour word!\n")

print "Correct!"