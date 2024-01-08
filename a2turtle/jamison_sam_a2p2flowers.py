import turtle

def turtInit ():
    #sets up the turtle 
    turtle.setup (width = 800, height = 800)
    turtle.shape(name = "turtle")
    turtle.speed (100)
    
    screen = turtle.screensize
turtInit ()

def setUp (x, y, color, w):
    #sets up teh turtle to draw flowers w location, color & line width
    turtle.penup ()
    turtle.goto (x, y)
    turtle.pendown ()
    turtle.color (color)
    turtle.fillcolor (color)
    turtle.width (w)

def flower1 ():
    #makes pink swirly flower
    setUp (-150, -200, "pink", 5)
    size = 7
    for x in range (6):
        for index in range (6):
            turtle.forward (size*x)
            turtle.left (30)
    turtle.forward (size*3)
    turtle.right (90)
    turtle.color ("green")
    turtle.forward (size*10)

def flower2 ():
    #makes cyan spikey flower
    setUp (-50, 150, "cyan", 3)
    size = 25
    turtle.begin_fill ()    
    for x in range (3):
        for index in range (3):
            turtle.forward (size*4)
            turtle.left (135)
    turtle.end_fill ()
    turtle.forward (size)
    turtle.right (135)
    turtle.color ("green")
    turtle.forward (size*2)

def flower3 ():
    #makes pruple square-y flower
    setUp (100, -200, "purple", 5)
    size = 8
    turtle.left (30)
    for x in range (6):
        for index in range (10):
            turtle.forward (size*x*3)
            turtle.left (90)
    turtle.forward (size*15)
    turtle.right (30)
    turtle.color ("green")
    turtle.forward (size*10)

flower1 ()
flower2 ()
flower3 ()
turtle.exitonclick()