import turtle
import random

sW = 1000
#screen width
sH = 700
#screen height

#turtle to write the score, sets up the game screen as well
turtle.setup (width = sW, height = sH)
turtle.bgcolor ("black")
turtle.shape(name = "turtle")
turtle.speed (100)
turtle.hideturtle ()
    
screen = turtle.screensize

#turtle to draw the middle line
arenaTurt = turtle.Turtle ()
arenaTurt.shape(name = "turtle")
arenaTurt.pencolor ("white")
arenaTurt.speed (100)
arenaTurt.hideturtle ()

def drawArena():
    #draws the line in the middle of the game screen
    arenaTurt.pensize (5)
    arenaTurt.goto (0, -sH/2)
    arenaTurt.goto (0, sH/2 + 10)
drawArena ()

#paddle 1 --  the paddle on the left
paddle1 = turtle.Turtle()
paddle1.shape("square")
paddle1.shapesize (stretch_wid = 7, stretch_len = 1)
paddle1.speed = 100
paddle1.color ("white")
paddle1.penup ()
p1x = -sW/2 + 25
p1y = 0
paddle1.goto (p1x, p1y)

#paddle 2 -- the paddle on the right
paddle2 = turtle.Turtle ()
paddle2.shape("square")
paddle2.shapesize (stretch_wid = 7, stretch_len = 1)
paddle2.speed = 100
paddle2.color ("white")
paddle2.penup ()
p2x = sW/2 - 32
p2y = 0
paddle2.goto (p2x, p2y)

#game ball
ball = turtle.Turtle ()
ball.shape("square")
ball.speed = 5
ball.color ("yellow")
ball.penup ()
ballx = 0
bally = 0
ball.goto (ballx, bally)
dx = random.randint (7, 12)
dy = random.randint (7, 12)

#moves paddle 1 up 15 units each time called
def up1 ():
    p1y = paddle1.ycor()
    p1y = p1y + 15
    if (p1y >= sH/2):
        p1y = p1y -15
    paddle1.goto (p1x, p1y)

#moves paddle 1 down 15 units each time called
def down1 ():
    p1y = paddle1.ycor()
    p1y = p1y - 15
    if (p1y <= -sH/2):
        p1y = p1y + 15    
    paddle1.goto (p1x, p1y)

#moves paddle 2 up 15 units each time called
def up2 ():
    p2y = paddle2.ycor()
    p2y = p2y + 15
    if (p2y >= sH/2):
        p2y = p2y -15
    paddle2.goto (p2x, p2y)

#moves paddle 2 down 15 units each time called
def down2 ():
    p2y = paddle2.ycor()
    p2y = p2y - 15
    if (p2y <= -sH/2):
        p2y = p2y + 15        
    paddle2.goto (p2x, p2y)

p1S = 0
#player 1 score
p2S = 0
#player 2 score

#writes both player's scores each time called, as well as clearing the previous scores
def writeScore ():
    turtle.clear ()  
    turtle.penup ()
    turtle.pencolor ("white")
    turtle.goto (-50, sH/2 - 50)
    turtle.write (p1S, font = ("Arial!", 25, "bold"))
    turtle.goto (50, sH/2 - 50)
    turtle.write (p2S, font = ("Arial!", 25, "bold"))
writeScore ()

#controls the paddle movements with w/s keys for the left paddle and up/down keys for the right
turtle.listen ()
turtle.onkeypress (up1, "w")
turtle.onkeypress (down1, "s")
turtle.onkeypress (up2, "Up")
turtle.onkeypress (down2, "Down")


while True:
    #checks if the ball is off of the screen on the right
    if (ball.xcor () >= sW/2):
        ball.hideturtle ()
        ball.goto (0, 0)
        ball.showturtle ()
        dx = -dx
        p1S += 1
        dx = random.randint (7, 12)
        dy = random.randint (7, 12)
        writeScore ()
    #checks if ball is off of the screen on the left        
    elif (ball.xcor () <= -sW/2):
        ball.hideturtle ()
        ball.goto (0, 0)
        ball.showturtle ()
        dx = -dx
        p2S += 1
        dx = random.randint (7, 12)
        dy = random.randint (7, 12)
        writeScore ()
    #checks if ball is off of the screen on the top or bottom
    elif (ball.ycor () >= sH/2 or ball.ycor () <= -sH/2):
        dy = -(dy)
    #checks if the ball is past or at paddle 1 xwise
    if (ball.xcor () <= paddle1.xcor () + 1):
        #if the ball is at paddle 1 xwise, checks if ball is at meeting paddle 1 ywise
        if (ball.ycor () <= paddle1.ycor () + 70 and ball.ycor () >= paddle1.ycor () - 70):
            dx = -dx
            dx = dx*1.3
            dy = dy*1.3
    #checks if the ball is past or at paddle 2 xwise
    if (ball.xcor () >= paddle2.xcor () - 1 and ball.ycor () >= paddle2.ycor () - 70):
        #if the ball is at paddle 2 xwise, checks if ball is at meeting paddle 2 ywise
        if (ball.ycor () <= paddle2.ycor () + 70):
            dx = -dx
            dx = dx*1.3
            dy = dy*1.3
    #moves the ball
    ballx = ball.xcor ()
    ballx += dx
    bally = ball.ycor ()
    bally += dy
    ball.goto (ballx, bally)

    #updates the screen
    turtle.update ()