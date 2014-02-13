#!/usr/bin/env python

"""
Write a program able to play the "Guess the number"-game, where the number to be guessed is randomly chosen between 1
and 20. (Source: http://inventwithpython.com)

This is how it should work when run in a terminal:

import guess_number
Hello! What is your name?
Torbjorn
Well, Torbjorn, I am thinking of a number between 1 and 20.
Take a guess.
10
Your guess is too low.
Take a guess.
15
Your guess is too low.
Take a guess.
18
Good job, Torbjorn! You guessed my number in 3 guesses!
"""

import random

name = raw_input("Hello! What is your name?\n")
print "Well, %s, I am thinking of a number between 1 and 20." % name

secret = random.randint(1, 20)
input = int(raw_input("Take a guess.\n"))
count = 1

while input != secret:
    if input < secret:
        print "Your guess is too low."
    elif input > secret:
        print "Your guess is too high."
    input = int(raw_input("Take a guess.\n"))
    count += 1

print "Good job, %s! You guessed my number in %d guesses!" % (name, count)