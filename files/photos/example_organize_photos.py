#!/usr/bin/env python3

"""
Code based on examples given in Udacity's Intro to Programming Nano-degree
Modified so that it takes command line arguments of subdirectories of the
directory you run it in. It iterates through the files in the specified
subdirectories and extracts the first word with underscores '_' on either
side and creates a sub directory of that name and moves the file into it.

"""

import os
import sys


def extract_place(f_name):
    """Extracts the portion of a string between two occurences of delimiter"""
    delimiter = '_'
    return f_name.split(delimiter)[1]


def make_place_directories(d_names):
    """creates a directory from a list of names passed to it"""
    for d_name in d_names:
        os.mkdir(d_name)


def organize_photos(directory):
    os.chdir(directory)
    originals = os.listdir()
    places = []

    for filename in originals:
        place = extract_place(filename)
        if place not in places:
            places.append(place)

    make_place_directories(places)

    for filename in originals:
        place = extract_place(filename)
        os.rename(filename, os.path.join(place, filename))


def main(argv):
    for directory in argv:
        organize_photos(directory)


if __name__ == "__main__":
    main(sys.argv[1:])
