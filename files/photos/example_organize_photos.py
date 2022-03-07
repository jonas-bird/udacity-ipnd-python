#!/usr/bin/env python3

"""
Code based on examples given in Udacity's Intro to Programming Nano-degree
"""

import os


def extract_place(f_name):
    """Extracts the portion of a string between two occurences of delimiter"""
    delimiter = '_'
    first = f_name[f_name.find(delimiter) + 1:]
    return first[:first.find(delimiter)]


os.chdir("Photos")
os.getcwd()
originals = os.listdir()

# Print out the list, just to be sure everything is correct (printf debugg)
print(originals)

testplace = extract_place(originals[0])
print(testplace)
