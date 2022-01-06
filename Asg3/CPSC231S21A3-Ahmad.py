# DO NOT EDIT THE FOLLOWING LINES
# COURSE CPSC 231 SPRING 2021
# INSTRUCTOR: Jonathan Hudson
# Wi52C3g7ZzkJ7XBcVRHY
# DO NOT EDIT THE ABOVE LINES

# INFORMATION FOR YOUR TA
# Haris Ahmad
# Tutorial T03
# 30088192
# 06/11/21
# This program will plot the given location and name of a star based off of files selected by the user

import sys
import os
import turtle

WIDTH = 600
HEIGHT = 600
TICK = 6
AXISLABEL = 12
AXISCOLOR = "blue"
BACKGROUNDCOLOR = "black"
STARCOLOR = "white"
STARCOLOR2 = "grey"

# This function will convert the values of X and Y to their pixel location on screen so it can fit
    # in a 600x600 screen size.
def convert(x,y):
    newX = 300 + (x * 300)
    newY = 300 + (y * 300)

    return newX, newY

# This function will change the color of the constellation outline and create a rotation so
    # that the colors cycle through.
def penColor(prevColor):
    newColor = prevColor % 3
    if newColor == 0:
        penColor = "red"
    elif newColor == 1:
        penColor = "green"
    else:
        penColor = "yellow"

    return penColor

# This function will draw the X and Y axes within the screen WIDTH/HEIGHT (600x600 pixels)
def makeAxes(pointer):
    pointer.color (AXISCOLOR)

# Drawing Y axis
    # Go to (300,0)
    pointer.goto(WIDTH/2, 0)
    pointer.down()

    # Go to (300,600)
    pointer.goto(WIDTH/2, HEIGHT)
    pointer.up()

# Drawing X axis
    # Go to (0, 300)
    pointer.goto(0, HEIGHT/2)
    pointer.down()

    # Go to (600, 300)
    pointer.goto(WIDTH, HEIGHT/2)
    pointer.up()
    drawXTicks(pointer)
    drawYTicks(pointer)

# This function will draw the ticks on the X axis and write the the increment value of +/-0.25
def drawXTicks(pointer):
    x = 0
    y = 0

    # Responsible for drawing the right side of the X axis (positive)
    while x <= 1:
        newX, newY = convert(x,y)
        pointer.goto(newX, newY)
        pointer.down()
        pointer.goto(newX, newY + TICK)
        pointer.goto(newX, newY - TICK)
        pointer.up()
        pointer.goto(newX, newY + AXISLABEL)
        if x != 0:
            pointer.write(str(x))
        x += 0.25
    x = 0
    y = 0

    # Responsible for drawing the left side of the X axis (negative)
    while x >= -1:
        newX, newY = convert(x,y)
        pointer.goto(newX, newY)
        pointer.down()
        pointer.goto(newX, newY + TICK)
        pointer.goto(newX, newY - TICK)
        pointer.up()
        pointer.goto(newX, newY + AXISLABEL)
        if x != 0:
            pointer.write(str(x))
        x -= 0.25

# This function will draw the ticks on the Y axis and write the the increment value of +/-0.25
def drawYTicks(pointer):
    x = 0
    y = 0

    # Responsible for drawing the top side of the Y axis (positive)
    while y <= 1:
        newX, newY = convert(x,y)
        pointer.goto(newX, newY)
        pointer.down()
        pointer.goto(newX + TICK, newY)
        pointer.goto(newX - TICK, newY)
        pointer.up()
        pointer.goto(newX + AXISLABEL, newY)
        if y != 0:
            pointer.write(str(y))
        y += 0.25
    x = 0
    y = 0

    # Responsible for bottom the right side of the Y axis (negative)
    while y >= -1:
        newX, newY = convert(x,y)
        pointer.goto(newX, newY)
        pointer.down()
        pointer.goto(newX + TICK, newY)
        pointer.goto(newX + TICK, newY)
        pointer.up()
        pointer.goto(newX + AXISLABEL, newY)
        if y!= 0:
            pointer.write(str(y))
        y -= 0.25

# This function checks to see if a file is found or not, if not the
    # the user is prompted to select a valid file.
def fileFound(file):
    error_code = 1

    while file != "":
        if os.path.isfile(file) == True:
            return file
        else:
            print (f"File {file} could not be found.")
            file = input("Please input a valid star location file: ")
    sys.exit(1)

# This function is used to check how many arguments are placed in the command line and computes a response
    # based on the length of the argument through the use of multiple if statements
def readArg():
    length = len(sys.argv)

    if length == 1:
        file = input("Please input a star location file: ")
        file = fileFound(file)
        names = False
        return file, names

    if length == 2:
        if sys.argv[1] == "-names":
            file = input("Please input a star location file: ")
            file = fileFound(file)
            names = True
            return file, names
        else:
            star_file = sys.argv[1]
            star_file = fileFound(star_file)
            names = False
            return star_file, names

    if length == 3:
        arg1 = sys.argv[1]
        arg2 = sys.argv[2]
        check1 = os.path.isfile(arg1)
        check2 = os.path.isfile(arg2)
        if (check1 == True) and (check2 == True):
            print("Neither argument included '-names'")
            sys.exit(0)
        if (check1 == False) and (check2 == False):
            print("Invalid input")
            sys.exit(0)
        if (check1 == True) or (arg1 == "-names"):
            if arg1 == "-names":
                file = fileFound(arg2)
                names = True
                return file, names
            if check1 == True:
                file = fileFound(arg1)
                if arg2 == "-names":
                    names = True
                    return file, names
        if (check1 == True) and (check2 == False):
            print(f"First argument:'{arg1}' is invalid")
            sys.exit(0)

    if length > 3:
        print("Too many arguments")
        sys.exit(0)

# This function receives a star file and splits it for each coma
def starData(data):
    try:
        # Star data is sorta based on its x,y,mag, or name
        data = data.split(",")
        x = float(data[0])
        y = float(data[1])
        mag = float(data[4])

        # Strips the newline as well to keep it consistent
        names = data[6].strip("\n")
        namelist = names.split(";")
        listlength = len(namelist)

        # If there is a name for the star, it splits it for each semicolon and stores
            # it in an organized format so it can be searched for easily in the dictionary
        if listlength == 1:
            name = namelist[0].lstrip(" ")
        else:
            name = ""
            for i in namelist:
                name += i.lstrip(" ")
                if i != namelist[listlength-1]:
                    name += ", "
        return x, y, mag, name

    # If the star file does not exist, this error message will be displayed and the program will exit
    except:
        print(" The given file was not a star location file")
        exit()

# This function plots the names on the grid based on user input ("-names")
def readDrawStars(file,pointer,names):
    # If the user did not input "-names", only the stars are drawn
    if names == False:
        stars = open(file)
        starlist = stars.readlines()
        length = len(starlist)
        counter = 1
        while counter <= length:
            data = starlist[counter-1]
            x, y, mag, name = starData(data)
            drawStar(x, y, mag, name, pointer)
            counter += 1
        stars.close()

   # If the user inputted "-names", the star names are displayed on the grid
    if names == True:
        stars = open(file)
        starlist = stars.readlines()
        length = len(starlist)
        counter = 1
        while counter <= length:
            data = starlist[counter-1]
            x, y, mag, name = starData(data)
            drawNames(x, y, name, pointer)
            counter += 1
        stars.close()

# This function identifies whether or not a star has a name
def drawStar(x,y,mag,name,pointer):
    newX, newY =  convert(x,y)
    radius = (10/(mag+2))/2
    pointer.up()
    pointer.goto(newX, newY - radius)

    # If the star has a name, it is plotted on the grid in the color white
    if name.strip("\n") != "":
        pointer.fillcolor(STARCOLOR)
        pointer.color(STARCOLOR)
        pointer.down()
        pointer.begin_fill()
        pointer.circle(radius)
        pointer.end_fill()

    # If the star has no name, it is plotted on the grid in the color grey
    else:
        pointer.fillcolor(STARCOLOR2)
        pointer.color(STARCOLOR2)
        pointer.down()
        pointer.begin_fill()
        pointer.circle(radius)
        pointer.end_fill()
    pointer.up()

# This function draws the name of the stars where they are located on the grid
def drawNames(x,y,name,pointer):
    newX, newY = convert(x,y)

    pointer.up()
    pointer.color(STARCOLOR)
    pointer.goto(newX, newY)
    pointer.write(name,font=("Arial",5,"normal"))
    pointer.up()

# This function draws a line between the stars that form a given constellation
def drawConstellation(x,y,newX,newY,pointer,counter):
    turtle.update()

    startX,startY = convert(x,y)
    endX, endY = convert(newX, newY)

    pointer.up()
    pointer.color(penColor(counter))
    pointer.goto(startX,startY)
    pointer.down()
    pointer.goto(endX,endY)
    pointer.up()

# This function is used to create a dictionary for the various stars plotted on the screen
def starDictionary(starFile):
    myStarDictionary = {}
    stars = open(starFile)
    starlist = stars.readlines()
    length = len(starlist)
    counter = 1

    # Identifying if the star has a name
    while counter <= length:
        data = starlist[counter-1]
        x,y,mag,name = starData(data)

        # If the star has a name it is added to the list, if not it is skipped
        if name != "":

            # If there are two or more names it is split by a comma
            if ", " in name:
                listofnames = name.split(", ")
                for Name in listofnames:
                    myStarDictionary[Name] = x,y
            else:
                myStarDictionary[name] = x,y
        counter += 1
    stars.close()
    return myStarDictionary

# This function is used to read the given constellation
def readConstellation(conFile,starfile,pointer,counter):
    try:
        # This section of code reads the file and puts it all in a list
        starDict = starDictionary(starfile)
        constell = open(conFile)
        conList = constell.readlines()
        constellName = conList[0].strip("\n")
        conLength = len(conList)
        colorCounter = counter
        starsContained = []
        counter = 1

        #
        while counter < conLength:
            # Gathering the name of the starting value and ending value
            namesForEdge = conList[counter].split(",")
            startName = namesForEdge[0].strip("\n")
            endName = namesForEdge[1].strip("\n")
            starsContained += (startName, endName)

            # Uses the values given as a key so the exact stars can be located in the dictionary
            first = starDict[startName]
            startX = first[0]
            startY = first[1]
            end = starDict[endName]
            endX = end[0]
            endY = end[1]
            drawConstellation(startX, startY, endX, endY, pointer, colorCounter)
            counter += 1

        # Deletes any duplicated entities in the list
        starsContained = sorted(set(starsContained), key = lambda x:starsContained.index(x))
        constell.close()

        # Prints out the stars used in creating the outline of the given constellation
        print(f"{constellName} constellation contains {starsContained}")
    except:
        print("The given file was not a constellation file")

# This function asks the user to input a constellation file
def inputConstellation(starFile, pointer):
    constellFile = input("Please enter in the constellation file name: ")
    counter = 1
    checkConstell = os.path.isfile(constellFile)

# While an invalid constellation file is inputted the user will be prompted to input a valid file
    # If "" is entered, then the loop will stop and the program will close
    while checkConstell == False and constellFile != "":
        constellFile = input("Please enter a valid constellation file name: ")
        checkConstell = os.path.isfile(constellFile)

# While the constellation file was found, the user will be prompted to keep re-entering files
    # If "" is entered, then the loop will stop and the program will close
    while constellFile != "" and checkConstell == True:
        readConstellation(constellFile, starFile,pointer,counter)
        counter +=1
        constellFile = input("Enter in another constellation filename: ")
        checkConstell = os.path.isfile(constellFile)
        while checkConstell == False and constellFile != "":
            constellFile = input("Enter in a valid constellation filename: ")
            checkConstell = os.path.isfile(constellFile)

    sys.exit(0)

# Sets up the turtle pointer
def setup():
    pointer = turtle.Turtle()
    pointer.speed(0)
    screen = turtle.getscreen()
    screen.setup(WIDTH, HEIGHT, 0, 0)
    screen.setworldcoordinates(0, 0, WIDTH, HEIGHT)
    pointer.hideturtle()
    screen.delay(delay=0)
    turtle.bgcolor(BACKGROUNDCOLOR)
    pointer.up()
    return pointer

def main():
    #Handle arguments
    file,names = readArg()
    #Read star information from file (function)
    turtle.tracer(0)
    pointer = setup()
    #Draw Axes (function)
    makeAxes(pointer)
    #Draw Stars (function)
    readDrawStars(file,pointer,names)
    turtle.update()
    #Loop getting filenames
    inputConstellation(file,pointer)
        #Read constellation file (function)
            # Already called within the "inputConstellation" function
        #Draw Constellation (function)
            # Already called within the "inputConstellation" function as well

main()
turtle.getscreen().exitonclick()
