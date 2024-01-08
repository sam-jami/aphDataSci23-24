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
screen.title('cocktail sort')
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


def cocktailSort(v):
#takes in list v and sorts it from l to r  
    count = 0
    #number of times thru the loop
    b = 0
    #used for breaking the loop later
    while (count < int(n/2)):
        #while the count is less than half of the list size, it loops thru the lsit & sorts from < to >
        for index in range (n - 1 - count):
            #checks if l > r, if so swaps them
            if (v[index] > v[index + 1]):
                #if l > r, swap
                higher = v[index]
                lower = v[index+1]
                v[index]=lower
                v[index+1]=higher
                b = 1
            turtle.clear()
            drawBars(v,n)
            screen.update()
        for index in range (n - 1 -count):
        #checks if l > r, if so swaps them
            if (v[n -index -1] < v[n -index -2]):
                #if r < l, swap
                higher = v[n-index-2]
                lower = v[n-index-1]
                v[n-index-2]=lower
                v[n-index-1]=higher
                b =1
            turtle.clear()
            drawBars(v,n)
            screen.update()
        if (b == 0):
            #if b is 0 (meaning that no bars were out of order), break
            break
        count += 1
        b = 0

t0 = time.time ()
cocktailSort(v)
t1 = time.time ()
print (t1-t0)

screen.exitonclick()