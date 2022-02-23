#!/usr/bin/env python3

import turtle
amy = turtle.Turtle()

# Make the width thicker so that the line will be easier to see
amy.width(5)

# Move back without drawing anything
amy.penup()
amy.back(140)
amy.pendown()

color_list = ["red", "orange", "yellow"]
# Draw three red lines, with space in between
for t_color in color_list:
    amy.color(t_color)
    amy.forward(50)
    amy.penup()
    amy.forward(50)
    amy.pendown()
