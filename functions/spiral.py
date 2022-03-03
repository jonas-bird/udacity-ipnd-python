#!/usr/bin/env python3

import turtle

def spiral(sides, turn, color, width):
"""
    draws a spiral with number of sides equal to sides
"""

    for n in range(sides):
        t.forward(n)
        t.right(30)
