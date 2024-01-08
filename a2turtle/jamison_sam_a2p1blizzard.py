import turtle
import random

def turtInit ():
    #sets up turtle
    turtle.setup (width = 800, height = 800)
    turtle.shape(name = "turtle")
    turtle.speed (100)
    turtle.color ("blue")
    
    screen = turtle.screensize
turtInit ()

sfSize = 50
branches = 4
legs = 10
armLen = sfSize/2
sfCount = 30
r = 0
g = 0
b = 0


def sf (sfSize, legs, branches, r, g, b):
    #draws one snowflake
    for index in range (legs):
        turtle.color (r, g, b)
        turtle.forward (sfSize/(branches/2))
        for index in range (branches):
            turtle.left (30)
            turtle.forward (armLen)
            turtle.forward(-armLen)
            turtle.right (30)
            turtle.right (30)
            turtle.forward (armLen)
            turtle.forward(-armLen)
            turtle.left (30)
            turtle.forward (sfSize/(branches/2))
        turtle.back(sfSize*2+sfSize/(branches/2))
        turtle.left (360/legs)
        turtle.pendown()

def moreSf ():
    #draws sfCount amt of snowflakes w randomized size, location, & colors
    for index in range (sfCount):
        turtle.penup ()
        x = random.uniform (-400, 400)
        y = random.uniform (-400, 400)
        turtle.goto (x, y)
        turtle.pendown ()
        turtle.seth (random.uniform (0, 360))
        sfSize = random.randint (10, 30)
        legs = random.randint (4, 12)
        branches = random.randint (1, 7)
        r = random.uniform(0,1)
        g = random.uniform(0,1)
        b = random.uniform(0,1)
        sf (sfSize, legs, branches, r, g, b)


moreSf ()
turtle.exitonclick()