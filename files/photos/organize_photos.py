#!/usr/bin/env python3

import os

os.chdir("Photos")
os.getcwd()
originals = os.listdir()

# Print out the list, just to be sure everything is correct (printf debugg)
print(originals)
