# DO NOT EDIT THE FOLLOWING LINES
# COURSE CPSC 231 SPRING 2021
# INSTRUCTOR: Jonathan Hudson
# OqdOu1Z6ZaT9zZ4f3myL
# DO NOT EDIT THE ABOVE LINES

# INFORMATION FOR YOUR TA
# Name: Haris Ahmad
# ID: 30088192
# Date: 2020-05-21
# Description: This program will locate the intersection point between a circle and a given line if there is one

import turtle
import math

WIDTH = 800
HEIGHT = 600

# PROVIDED CODE
# NEED TO SET WIDTH AND HEIGHT TO USE
# Setup the world (get objects, set screen size and coordinate system, hide pointer)
pointer = turtle.Turtle()
screen = turtle.getscreen()
screen.setup(WIDTH, HEIGHT, 0, 0)
screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
pointer.hideturtle()
#screen.delay(delay=0)
# END PROVIDED CODE

#PROGRAM
#This section of code is responsible for making the X and Y axis'
pointer.speed(0)

pointer.up()
pointer.goto(400, 0)
pointer.down()
pointer.goto(400, 600)
pointer.up()
pointer.goto(0, 300)
pointer.down()
pointer.goto(800, 300)
pointer.hideturtle()

# Describing to the user what the program does
print("This program will plot a circle and a line somewhere on the screen based on user input")
print("The program will then determine the intersection points between the line and the circle if any exist")
print("The cross section of the X and Y axis' is at (400,300)")
print("The bottom left corner is at (0,0) and the top right corner is at (800,600)")
print("Please provide input for the following prompts. \n \n")

# Asking the user to input the values for the circle
circleX = int(input("Enter circle x coordinate: "))
circleY = int(input("Enter circle y coordinate: "))
circleRadius = float(input("Enter radius of circle: "))

# Calculations so that the centre of the circle will be at the points the user inputted
circleCentre = circleY - circleRadius

# The code for drawing the circle
pointer.pencolor("red")
pointer.up()
pointer.goto(circleX, circleCentre)
pointer.down()
pointer.circle(circleRadius, 360)

# Asking the user to input the starting and ending points of the line
startingX = int(input("Enter line start x coordinate: "))
startingY = int(input("Enter line start y coordinate: "))
endingX = int(input("Enter line end x coordinate: "))
endingY = int(input("Enter line end y coordinate: "))

# The code for drawing the line
pointer.pencolor("blue")
pointer.up()
pointer.goto(startingX, startingY)
pointer.down()
pointer.goto(endingX, endingY)
pointer.up()

# Constants used for the quadratic formula
A = (endingX - startingX)**2 + (endingY - startingY)**2
B = 2 * (((startingX - circleX) * (endingX - startingX)) + ((startingY - circleY) * (endingY - startingY)))
C = (startingX - circleX)**2 + (startingY - circleY)**2 - (circleRadius)**2

RADICAND = (B**2 - 4*A*C)
greaterThanZero = (RADICAND > 0)
lessThanZero = (RADICAND < 0)
equalsZero = (RADICAND == 0)

# Setting the possible intersection points color to green
pointer.up()
pointer.color("green")

# The possible options that could occur depending on how many intersections occur
# If there are no intersections this decision will be chosen and an appropriate message will display to the user
if lessThanZero:
    pointer.goto(340, 300)
    pointer.write("NO INTERSECTION POINTS!")

# If the radicand is not less than zero this decision will be chosen
if not lessThanZero:
    # If the radicand is equal to zero this decision will be chosen
    if greaterThanZero:

        SQUARE = math.sqrt(RADICAND)
        alphaPositive = (0-B + SQUARE)/(2*A)
        alphaNegative = (0-B - SQUARE)/(2*A)

        firstIntersectionX = (1 - alphaPositive)*startingX + (alphaPositive * endingX)
        firstIntersectionY = (1 - alphaPositive)*startingY + (alphaPositive * endingY)

        secondIntersectionX = (1 - alphaNegative)*startingX + (alphaNegative * endingX)
        secondIntersectionY = (1 - alphaNegative)*startingY + (alphaNegative * endingY)

        # A set of decisions that determine where to plot both points of the intersection
        if alphaPositive >= 0 and alphaPositive <= 1:
            pointer.goto(firstIntersectionX, firstIntersectionY)
            pointer.down()
            pointer.circle(5)
            pointer.up()
        if alphaNegative >= 0 and alphaNegative <= 1:
            pointer.goto(secondIntersectionX, secondIntersectionY)
            pointer.down()
            pointer.circle(5)
            pointer.up()

    # If the radicand equals zero this decision will be selected and only the 1 intersection point will be plotted
    elif equalsZero:
        SQUARE = math.sqrt(RADICAND)

        alphaPositive = (0-B + SQUARE)/(2*A)
        firstIntersectionX = (1 - alphaPositive)*startingX + (alphaPositive * endingX)
        firstIntersectionY = (1 - alphaPositive)*startingY + (alphaPositive * endingY)

        pointer.goto(firstIntersectionX, firstIntersectionY)
        pointer.down()
        pointer.circle(5)

screen.exitonclick()
