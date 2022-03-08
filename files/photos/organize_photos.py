#!/usr/bin/env python3

import os


def extract_place(f_name, delimiter):
    """Extracts the portion of a string between two occurences of delimiter"""
    first = f_name[f_name.find(delimiter) + 1:]
    return first[:first.find(delimiter)]


os.chdir("Photos")
os.getcwd()
originals = os.listdir()

# Print out the list, just to be sure everything is correct (printf debugg)
print(originals)
