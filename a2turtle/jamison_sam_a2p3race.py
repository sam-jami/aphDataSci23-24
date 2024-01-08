#ask: font size

import turtle
import random
line = ""

def turtInit ():
    #creates the black turtle that draw the track

    turtle.setup (width = 800, height = 800)
    turtle.shape(name = "turtle")
    turtle.speed (200)
    turtle.width (3)
    
    screen = turtle.screensize
turtInit ()

def redTurtInit ():
    #creates the red turtle
    redTurt.shape(name = "turtle")
    redTurt.speed = 100
    redTurt.color ("red")
    redTurt.width (5)
    redTurt.penup ()
    redTurt.goto (-370, 225)
    redTurt.pendown ()

def yellowTurtInit ():
    #creates the yellow turtle

    yellowTurt.shape(name = "turtle")
    yellowTurt.speed = 100
    yellowTurt.color ("yellow")
    yellowTurt.width (5)
    yellowTurt.penup ()
    yellowTurt.goto (-370, 75)
    yellowTurt.pendown ()

def greenTurtInit ():
    #creates the green turtle

    greenTurt.shape(name = "turtle")
    greenTurt.speed = 100
    greenTurt.color ("green")
    greenTurt.width (5)
    greenTurt.penup ()
    greenTurt.goto (-370, -75)
    greenTurt.pendown ()

def blueTurtInit ():
    #creates the blue turtle

    blueTurt.shape(name = "turtle")
    blueTurt.speed = 100
    blueTurt.color ("blue")
    blueTurt.width (5)
    blueTurt.penup ()
    blueTurt.goto (-370, -225)
    blueTurt.pendown ()


def turtRaceTrack ():
#makes the black turtle draw the racetrack for the other turtles to race on
    turtle.left (90)
    for lineMark in range (19):
        turtle.penup ()
        turtle.goto (-370 + lineMark*40, -350)
        line = str(lineMark)
        for index in range (15):
            turtle.forward (20)
            turtle.penup ()
            turtle.forward (23)
            turtle.pendown ()
        turtle.write (line, font = ("Arial!", 16, "bold"))
    turtle.penup()
    turtle.goto (-370, 355)

def turtSpawn ():
#uses the racer turtle functions to initiate the turtles and send them to their spots
    redTurtInit ()
    yellowTurtInit ()
    greenTurtInit ()
    blueTurtInit ()

def turtRace ():
#makes the colored turtles race & delcares a winner
    redForward = random.randint (20, 30)
    yellowForward = random.randint (20, 30)
    greenForward = random.randint (20, 30)
    blueForward = random.randint (20, 30)
    for index in range (100):
        redTurt.forward (redForward)
        yellowTurt.forward (yellowForward)
        greenTurt.forward (greenForward)
        blueTurt.forward (blueForward)
        if (redTurt.xcor() >= 370):
            turtle.write ("red won!", font = ("Arial!", 16, "bold"))
            turtle.goto (1000, 1000)
            break
        elif (yellowTurt.xcor() >= 370):
            turtle.write ("yellow won!", font = ("Arial!", 16, "bold"))
            turtle.goto (1000, 1000)
            break
        elif (greenTurt.xcor() >= 370):
            turtle.write ("green won!", font = ("Arial!", 16, "bold"))
            turtle.goto (1000, 1000)
            break
        elif (blueTurt.xcor() >= 370):
            turtle.write ("blue won!", font = ("Arial!", 16, "bold"))
            turtle.goto (1000, 1000)
            break


    
        

turtRaceTrack ()

redTurt=turtle.Turtle()
yellowTurt=turtle.Turtle()
greenTurt=turtle.Turtle()
blueTurt=turtle.Turtle()

turtSpawn ()
turtRace ()
    

turtle.exitonclick()