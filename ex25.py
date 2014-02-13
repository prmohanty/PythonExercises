#!/usr/bin/env python

"""
In English, the present participle is formed by adding the suffix -ing to the infinite form: go -> going.
A simple set of heuristic rules can be given as follows:

    a. If the verb ends in e, drop the e and add ing (if not exception: be, see, flee, knee, etc.)
    b. If the verb ends in ie, change ie to y and add ing
    c. For words consisting of consonant-vowel-consonant, double the final letter before adding ing
    d. By default just add ing

Your task in this exercise is to define a function make_ing_form() which given a verb in infinitive form returns its
present participle form. Test your function with words such as lie, see, move and hug. However, you must not expect such
simple rules to work for all cases.
"""

from ex4 import is_vowel


def make_ing_form(verb):
    if verb.endswith('ie'):
        return verb[:-2] + 'ying'
    elif verb.endswith('e') and (verb[-2].endswith('e') or len(verb) == 2):
        return verb + 'ing'
    elif verb.endswith('e'):
        return verb[:-1] + 'ing'
    elif not is_vowel(verb[-1]) and is_vowel(verb[-2]) and not is_vowel(verb[-3]):
        return verb + verb[-1] + 'ing'
    else:
        return verb + 'ing'


if __name__ == "__main__":
    print make_ing_form('be')
    print make_ing_form('lie')
    print make_ing_form('see')
    print make_ing_form('move')
    print make_ing_form('hug')