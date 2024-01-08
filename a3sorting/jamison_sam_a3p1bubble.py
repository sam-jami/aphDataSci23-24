import turtle
import random
import time

t0 = 0
#t0: time one
t1 = 0
#t1: end time
tf = 0
#tf final time

n = 50
#n: length of list
v = [0] * n
#v: name of list

for i in range(n):
    #creates an empty list (v) and then fills it with random values
    v[i] = random.randint(1,800)

#sets up the screen
screen = turtle.Screen()
screen.setup(1000,1000)
screen.tracer(0,0)
#name for the window that is opened
screen.title('bubble sort')
turtle.speed(0)
turtle.hideturtle()

def drawBar(x,y,w,h):
#draws a bar at the specified x and y coordinate with width w and height h    
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(0)
    turtle.down()
    turtle.fillcolor ("pink")
    turtle.begin_fill()
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h)
    turtle.left(90)
    turtle.end_fill()

def drawBars(v,n):
#draws n bars using height values and order from list v    
    x = -400
    w = 800/n
    for  i in range(n):
        #for the length of the list, draws that amt of bars
        drawBar(x,-400,w,v[i])
        x += w

def bubbleSort(v):
#takes in list v and sorts it from l to r  
    for index in range (n):
        #loops thru entire list, ordering from < to >
        for index in range (n - 1 - index):
            #checks if l > r, if so swaps them
            if (v[index] > v[index + 1]):
                #if l > r, swap
                higher = v[index]
                lower = v[index+1]
                v[index]=lower
                v[index+1]=higher
                turtle.clear()
                drawBars(v,n)
                screen.update()

t0 = time.time ()
bubbleSort(v)
t1 = time.time ()
print (t1-t0)

#End TODO 2: Dont write beyond this.

screen.exitonclick()