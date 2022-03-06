#!/usr/bin/env python3
"""Example from repeating with functions 1/2"""


def simple_recursion():
    response = input("Can you guess what my favorite color is?\n")
    if response != 'blue':
        simple_recursion()
    else:
        print("That's right! My favorite color is blue.")


simple_recursion()
