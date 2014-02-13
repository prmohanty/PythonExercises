#!/usr/bin/env python

"""
Represent a small bilingual lexicon as a Python dictionary in the following fashion
{"merry":"god", "christmas":"jul", "and":"och", "happy":gott", "new":"nytt", "year":"ar"}
and use it to translate your Christmas cards from English into Swedish.
That is, write a function translate() that takes a list of English words and returns a list of Swedish words.
"""


def translate(words):
    lexicon = {"merry": "god", "christmas": "jul", "and": "och", "happy": "gott", "new": "nytt", "year": "ar"}
    return [lexicon[word] for word in words]


if __name__ == "__main__":
    print translate(['merry', 'christmas'])