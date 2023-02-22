####################################################################################
# Author:                           TODO: Change this to your name
# Username:                         TODO: Change this to your username
#
# Assignment: E1 - Coding Portion
# Purpose: Evaluate your ability to write code in Python
# Value: 35 points total
#
# Instructions:
#   Complete ALL of the tasks indicated below. Read carefully!
#   Even if you do not complete all tasks, submit what you complete before the class period ends.
#   Anything pushed after the class end time will not be considered while grading.
#   You may use the Python documentation, your own code, any code we've given you as part of this class,
#       and the online book. No other resources, especially no Googling!
#   You must do this alone without a partner and without help from your classmates.
#
# Overview:
#   This program draws a lovely array of rainy raindrops (because Spring!).
#
####################################################################################
#
# TODO A successful student will have completed the following tasks:
#   Task 1: Refactor the code to use a main() function. (8 pts)
#   Task 2: Ask the user to input a number between 1 and 10.  (5 pts)
#   Task 3: Call the draw_rainstorm function, indicating how many raindrops to draw using the user's
#      input from Task 2. (6 pts)
#   Task 4: Fix the draw_rainstorm() function by converting it to use a loop and iterate the right number
#      of times. (10 pts)
#   Task 5: Add docstrings and comments where appropriate, modify this header, and clean up any unused code. (6 pts)
#   Bonus: Include a new function that writes "It's February!" to the turtle screen.
#          modify main() to use this new function correctly IF the user picked four. (+1 pt)
#   Bonus: Modify the code so that each new raindrop is drawn with random x and y coordinates between -200 and
#          inclusive. (+1 pt)
#   Bonus: Also modify the code to randomize the color of each raindrop. (+1 pt)
#   Bonus: Also ALSO modify the code to give each raindrop a random radius between 10 and 60 inclusive. (+1 pt)
#   BONUS BONUS: Complete all four bonus tasks. (+1 pt)


####################################################################################
# Submission Instructions:
# Use git to commit and push your changes to the GitHub repository.
# Make sure your push is complete before the end of class!
####################################################################################

import turtle

def colors(col):
    """
    Returns a color.
    DO NOT MODIFY!!!

    :param col: color number, an integer from 0 to 4 inclusive
    :return: String representing a color
    """
    if col == 0:
        return "turquoise"
    elif col == 1:
        return "lightblue"
    elif col == 2:
        return "blue"
    elif col == 3:
        return "white"
    elif col == 4:
        return "skyblue"

def draw_circle(t, radius=30):
    """
    This function draws a circle as part of a raindrop.
    DO NOT MODIFY!!!

    :param t: an instance of the turtle class
    :param radius: an integer representing the radius of the circle
    :return: None
    """
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_triangle(t, length=60):
    """
    This function draws an equilateral triangle as part of a raindrop.
    DO NOT MODIFY!!!

    :param t: an instance of the turtle class
    :param length: an integer representing the side length of the triangle
    :return: None
    """
    t.seth(0)
    t.begin_fill()
    for i in range(3):
        t.left(120)
        t.forward(length)
    t.end_fill()

def draw_drop(t, mycolor='blue'):
    """
    This function draws a single raindrop on the screen.
    DO NOT MODIFY!!!

    :param t: an instance of the Turtle class
    :param mycolor: a string representing a color
    :return: None
    """
    t.color(mycolor)
    draw_circle(t)
    x, y = t.pos()
    t.goto(x + 30, y + 30)
    draw_triangle(t)

def move(t):
    """
    Moves a turtle object 30 pixels to the right and 50 pixels down.
    DO NOT MODIFY!!!

    :param t: an instance of the Turtle class
    :return: None
    """
    t.penup()
    t.setpos(t.xcor() + 30, t.ycor() - 50)
    t.pendown()

def draw_rainstorm(t, numdrops):
    '''

    :param t:
    :param numdrops:
    :return:
    '''

    # TODO Complete the docstring for this function. Follow the format of the other docstrings in this file.

    # TODO   This code is inefficient and inflexible. Rewrite the code below to use a loop
    #        the right number of times, based on the input parameters.

    draw_drop(t, mycolor=colors(0 % 5))
    move(t)
    draw_drop(t, mycolor=colors(1 % 5))
    move(t)
    draw_drop(t, mycolor=colors(2 % 5))
    move(t)
    draw_drop(t, mycolor=colors(3 % 5))
    move(t)
    draw_drop(t, mycolor=colors(4 % 5))
    move(t)

# The program starts running here
# TODO  Refactor this program to use a main() function. The highest level of the program should include
#       import statements, function definitions, and a call to main() ONLY.  No lonely lines of code
#       outside of functions!

w = turtle.Screen()
w.bgcolor('gray')
t = turtle.Turtle()

t.speed(15)
t.penup()
t.setpos(-250, 150)
t.pendown()


# TODO   Ask the user to input a number between 1 and 10.

# TODO   Call the draw_rainstorm function, indicating how many raindrops to draw using the user's
#  input (instead of four)

draw_rainstorm(t, 4)

w.exitonclick()
