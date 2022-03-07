#!/usr/bin/env python3

"""
Code based on examples given in Udacity's Intro to Programming Nano-degree
"""

import os


def extract_place(f_name):
    """Extracts the portion of a string between two occurences of delimiter"""
    delimiter = '_'
    return f_name.split(delimiter)[1]


def make_place_directories(d_names):
    """creates a directory from a list of names passed to it"""
    for d_name in d_names:
        os.mkdir(d_name)


os.chdir("Photos")
originals = os.listdir()
places = []

for files in originals:
    places.append(extract_place(files))
make_place_directories(places)
print(os.listdir())
