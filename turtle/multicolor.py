#!/usr/bin/env python3

import turtle

color_collection = ["green", "yellow", "purple", "orange", "red", "gray", "black", "blue"]


# Write whatever code you want here!
aOC = turtle.Turtle()
aOC.width(5)
aOC.speed(0)
arrow_direction = 45

for color in color_collection:
    aOC.color(color)
    aOC.right(arrow_direction)
    aOC.forward(100)
    aOC.left(130)
    aOC.forward(20)
    aOC.back(20)
    aOC.left(100)
    aOC.forward(20)
    aOC.back(20)
    # get the turtle pointed in the direction of the arrow and back to the center
    aOC.left(130)
    aOC.back(100)
aOC.hideturtle()
turtle.done()
