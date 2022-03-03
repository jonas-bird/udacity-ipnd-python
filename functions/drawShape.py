#!/usr/bin/env python3

import turtle

def draw_spiral(sides, turn, color, width):
"""
    draws a spiral with number of sides equal to sides
"""
    t = turtle.Turtle()
    t.color(color)
    t.width(width)
    for n in range(sides):
        t.forward(n)
        t.right(turn)


def draw_square(length, l_color, l_width):
    jack = turtle.Turtle()
    jack.color(l_color)
    jack.width(l_width)
    for side in range(4):
        jack.forward(length)
        jack.right(90)


# def draw_shape(color, length, number_sides):
#     jack.color(color)
#     for i in range(sides):
#         jack.forward(length)
#         jack.right(360/number_sides)
def draw_shape(line_color, line_weight, number_sides, sides_length):
    t = turtle.Turtle()
    t.color(line_color)
    t.width(line_weight)
    try:
        angle = 360/number_sides
    except ZeroDivisionError:
        print("Invalid number of sides")
        return 0
    for i in range(number_sides):
        t.forward(sides_length)
        t.right(angle)


number_sides = 50
length_sides = 30
line_color = "blue"
line_width = 3
draw_spiral(number_sides, length_sides, line_color, line_width)
length_sides = 100
line_color = "yellow"
draw_square(length_sides, line_color, line_width)
turtle.done()
