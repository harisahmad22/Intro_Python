# DO NOT EDIT THE FOLLOWING LINES
# COURSE CPSC 231 SPRING 2021
# INSTRUCTOR: Jonathan Hudson
# ZLMFYxeVpu8JUdbLOmen
# DO NOT EDIT THE ABOVE LINES

# INFORMATION FOR YOUR TA
# Haris Ahmad
# Tutorial T03
# 30088192
# 05/28/21
# This program will graph various different lines on the screen, based off of user input

from math import *
import turtle

# CONSTANTS
WIDTH = 800
HEIGHT = 600
AXISCOLOR = "black"
TICK = 5
textLocation = 20

#
#  Returns the screen (pixel based) coordinates of some (x, y) graph location base on configuration
#
#  Parameters:
#   xo, yo : the pixel location of the origin of the  graph
#   ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#   x, y: the graph location to change into a screen (pixel-based) location
#
#  Usage -> screenCoor(xo, yo, ratio, 1, 0)
#
#  Returns: (screenX, screenY) which is the graph location (x,y) as a pixel location in the window
#
def screenCoor(xo, yo, ratio, x, y):
    screenX = (xo + (ratio * x))
    screenY = (yo + (ratio * y))

    return screenX, screenY

#
#  Returns a string of the colour to use for the current expression being drawn
#  This colour is chosen based on which how many expression have previously been drawn
#  The counter starts at 0, the first or 0th expression, should be red, the second green, the third blue
#  then loops back to red, then green, then blue, again
#
#  Usage -> getColor(counter)
#
#  Parameters:
#  counter: an integer where the value is a count (starting at 0) of the expressions drawn
#
#  Returns: 0 -> "red", 1 -> "green", 2 -> "blue", 3 -> "red", 4 -> "green", etc.
#
def getColor(counter):
    color = counter % 3

    if color % 3 == 0:
        penColor = "red"
    elif color % 3 == 1:
        penColor = "green"
    elif color % 3 == 2:
        penColor = "blue"

    return penColor

#
#  Draw in the window an xaxis label (text) for a point at (screenX, screenY)
#  the actual drawing points will be offset from this location as necessary
#  Ex. for (x,y) = (1,0) or x-axis tick/label spot 1, draw a tick mark and the label 1
#
#  Usage -> drawXAxisLabelTick(pointer, 1, 0, "1")
#
#  Parameters:
#  pointer: the turtle drawing object
#  screenX, screenY): the pixel screen location to drawn the label and tick mark for
#  text: the text of the label to draw
#
#  Returns: Nothing
#
def drawXAxisLabelTick(pointer, changedX, changedY, x):
    pointer.goto(changedX, changedY)
    pointer.down()
    pointer.goto(changedX, changedY + TICK)
    pointer.goto(changedX, changedY)
    pointer.goto(changedX, changedY - TICK)
    pointer.goto(changedX, changedY)
    pointer.up()
    pointer.goto(changedX, changedY - textLocation)

    if x != 0:
        pointer.write(str(x))

    pointer.goto(changedX, changedY)
#
#  Draw in the window an yaxis label (text) for a point at (screenX, screenY)
#  the actual drawing points will be offset from this location as necessary
#  Ex. for (x,y) = (0,1) or y-axis tick/label spot 1, draw a tick mark and the label 1
#
#  Usage -> drawXAxisLabelTick(pointer, 0, 1, "1")
#
#  Parameters:
#  pointer: the turtle drawing object
#  screenX, screenY): the pixel screen location to drawn the label and tick mark for
#  text: the text of the label to draw
#
#  Returns: Nothing
#
def drawYAxisLabelTick(pointer, changedX, changedY, y):

    pointer.goto(changedX, changedY)
    pointer.down()
    pointer.goto(changedX + TICK, changedY)
    pointer.goto(changedX, changedY)
    pointer.goto(changedX - TICK, changedY)
    pointer.goto(changedX, changedY)
    pointer.up()
    pointer.goto(changedX - textLocation,changedY)

    if y != 0:
        pointer.write(str(y))

    pointer.goto(changedX,changedY)

#
#  Calculates the maximum and minimum axis length (positive and negative for both the X and Y axis)
#
#  Usage -> maxMinAxis(HEIGHT, WIDTH, xo, yo, ratio)
#
#  Parameters:
#  HEIGHT: the turtle drawing object
#  WIDTH: the pixel location of the origin of the  graph
#  xo: the starting value in pixels for X coordinate
#  yo: the starting value in pixels for Y coordinate
#  ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#
#  Returns: (negativeYAxis, positiveYAxis, negativeXAxis, positiveXAxis) which is the max of each plane (each quadrant)
#
def maxMinAxis(HEIGHT, WIDTH, xo, yo, ratio):
    negativeYAxis = 0 - ((yo//ratio) + 1)
    positiveYAxis = (HEIGHT//ratio - yo//ratio) + 1
    negativeXAxis = 0 - ((xo//ratio) + 1)
    positiveXAxis = (WIDTH//ratio - xo//ratio) + 1

    return negativeYAxis, positiveYAxis, negativeXAxis, positiveXAxis

#
#  Draw in the window an xaxis (secondary function is to return the minimum and maximum graph locations drawn at)
#
#  Usage -> drawXAxis(pointer, xo, yo, ratio)
#
#  Parameters:
#  pointer: the turtle drawing object
#  xo, yo : the pixel location of the origin of the  graph
#  ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#
#  Returns: (xmin, ymin) where xmin is minimum x location drawn at and xmax is maximum x location drawn at
#

def drawXAxis(pointer, xo, yo, ratio):
    pointer.up()
    pointer.goto(xo,yo)
    x = 0
    y = 0

    negativeYAxis, positiveYAxis, negativeXAxis, positiveXAxis = maxMinAxis(HEIGHT, WIDTH, xo, yo, ratio)

    while x <= positiveXAxis:
        newX, newY = screenCoor(xo, yo, ratio, x, y)
        pointer.down()
        pointer.goto(newX,yo)
        drawXAxisLabelTick(pointer, newX, newY, x)
        x += 1
    xmax = x
    x = 0
    while x >= negativeXAxis:
        newX, newY = screenCoor(xo, yo, ratio, x, y)
        pointer.down()
        pointer.goto(newX,yo)
        drawXAxisLabelTick(pointer, newX, newY, x)
        x -= 1
    xmin = x

    return xmin, xmax

#
#  Draw in the window an yaxis
#
#  Usage -> drawYAxis(pointer, xo, yo, ratio)
#
#  Parameters:
#  pointer: the turtle drawing object
#  xo, yo : the pixel location of the origin of the  graph
#  ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#
#  Returns: Nothing
#
def drawYAxis(pointer, xo, yo, ratio):
    pointer.goto(xo,yo)
    x = 0
    y = 0
    negativeYAxis, positiveYAxis, negativeXAxis, positiveXAxis = maxMinAxis(HEIGHT, WIDTH, xo, yo, ratio)
    while y <= positiveYAxis:
        newX, newY = screenCoor(xo, yo, ratio, x, y)
        pointer.down()
        pointer.goto(xo,newY)
        drawYAxisLabelTick(pointer, newX, newY, y)
        y += 1
    ymax = y
    y = 0
    while y >= negativeYAxis:
        newX, newY = screenCoor(xo, yo, ratio, x, y)
        pointer.down()
        pointer.goto(xo,newY)
        drawYAxisLabelTick(pointer, newX, newY, y)
        y -= 1
    ymin = y

    return ymin, ymax
#
#  Draw in the window the given expression (expr) between [xmin, xmax] graph locations
#
#  Usage -> drawExpr(pointer, xo, yo, ratio, xmin, xmax, expr)
#
#  Parameters:
#  pointer: the turtle drawing object
#  xo, yo : the pixel location of the origin of the  graph
#  ratio: the ratio of pixels to single step in graph (i.e 1 step is ratio amount of pixels)
#  expr: the expression to draw (assumed to be valid)
#  xmin, ymin : the range for which to draw the expression [xmin, xmax]
#
#  Returns: Nothing
#
def drawExpr(pointer, xo, yo, ratio, xmin, xmax, expr):
    pointer.up()
    delta = 0.1
    x = xmin
    while x <= xmax:
        x += delta
        y = eval(expr)
        pointer.goto(x*ratio + xo, y*ratio + yo)
        pointer.down()

    pointer.up()

#
#  Setup of turtle screen before we draw
#  DO NOT CHANGE THIS FUNCTION
#
#  Returns: Nothing
#
def setup():
    pointer = turtle.Turtle()
    screen = turtle.getscreen()
    screen.setup(WIDTH, HEIGHT, 0, 0)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    pointer.hideturtle()
    screen.delay(delay=0)
    return pointer

#
#  Main function that attempts to graph a number of expressions entered by the user
#  The user is also able to designate the origin of the chart to be drawn, as well as the ratio of pixels to steps (shared by both x and y axes)
#  The window size is always 800 width by 600 height in pixels
#  DO NOT CHANGE THIS FUNCTION
#
#  Returns: Nothing
#
def main():
    #Setup window
    pointer = setup()

    #Get input from user
    xo = int(input("Enter pixel coordinates of origin x: "))
    yo = int(input("Enter pixel coordinates of origin y: "))
    ratio = int(input("Enter ratio of pixels per step: "))

    #Set color and draw axes (store discovered visible xmin/xmax to use in drawing expressions)
    pointer.color(AXISCOLOR)
    xmin, xmax = drawXAxis(pointer, xo, yo, ratio)
    drawYAxis(pointer, xo, yo, ratio)

    #Loop and draw experssions until empty string "" is entered, change expression colour based on how many expressions have been drawn
    expr = input("Enter an arithmetic expression: ")
    counter = 0
    while expr != "":
        pointer.color(getColor(counter))
        drawExpr(pointer, xo, yo, ratio, xmin, xmax, expr)
        expr = input("Enter an arithmetic expression: ")
        counter += 1

#Run the program
main()
turtle.getscreen().exitonclick()
