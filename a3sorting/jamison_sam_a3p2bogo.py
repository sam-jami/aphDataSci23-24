import turtle
import random
import time

t0 = 0
#t0: time one
t1 = 0
#t1: end time
tf = 0
#tf final time
check = 0

n = 5
#length of list
v = [0] * n
#v: name of list

for i in range(n):
    #creates an empty list and then fills it with random values
    v[i] = random.randint(1, 30)

#sets up the screen
screen = turtle.Screen()
screen.setup(1000,1000)
screen.tracer(0,0)
#name for the window that is opened
screen.title('bogo sort')
turtle.speed(0)
turtle.hideturtle()

def drawBar(x,y,w,h):
    #draws a bar at the specified x and y coordinate with width w and height h
    r = random.randint (0,1)
    g = random.randint (0,1)
    b = random.randint (0, 1)
    turtle.up()
    turtle.goto(x,y)
    turtle.seth(0)
    turtle.down()
    turtle.fillcolor (r, g, b)
    turtle.begin_fill()
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h*20)
    turtle.left(90)
    turtle.fd(w)
    turtle.left(90)
    turtle.fd(h*20)
    turtle.left(90)
    turtle.end_fill()

def drawBars(n, v):
    #draws n bars using height values & order from list v
    x = -400
    w = 800/n
    for i in range(n):
        #for the length of the list, draws that amt of bars
        drawBar(x,-400,w,v[i])
        x += w

def swapList (n, v):
    #swaps values of list
    x = 0
    y = 0
    #index: current place in list
    #place: place in list that is being swapped w index
    #v: list
    for index in range (n-1):
        #swaps the whole list by going value by value & swapping it with a random other value
        place = random.randint(0,n-1)
        temp = v[index]
        v[index] = v[place]
        v[place] = temp
    return v

def checkList (n, v):
    #checks if list is sorted, returns 0 if not & 1 if so to bogoSort
    for index in range (n - 1):
        #checks if l > r, if it is then ends loop & returns 0 to bogoSort
        if (v[index] > v[index + 1]):  
           #if l > r, return 0
           return 0
    return 1

def bogoSort(v, check):
    #checks if the list is sorted, if not then continues to swap & check again until it is
    while (check == 0):
        #as long as the list is unsorted, it swaps it then checks again
        swapList (n, v)
        turtle.clear()
        drawBars(n, v)
        screen.update()
        check = checkList (n, v)

def timer ():
    #subtracts end time from beginning time to give a total time of sorting
    t0 = time.time ()
    bogoSort(v, check)
    t1 = time.time ()
    print (t1-t0)
    
timer ()

screen.exitonclick()