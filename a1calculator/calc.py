
def add (x, y):
    result = x + y
    return (result)
def sub (x, y):
    result = x - y
    return (result)
def mult (x, y):
    result = x * y
    return (result)
def div (x, y):
    result = x / y
    return (result)
def exp (x, y):
    x2 = x
    for e in range (1, y):
        x = x * x2
    result = x
    return (result)

def split (equ):
    """take in equation, return what is before the first space"""
    first = equ.find (" ")
    bef = equ[0:first]
    aft = equ[first + 1:len(equ)]
    return (bef, aft)    

def math (equ):
    x, x2 = split (equ)
    x = int(x)
    op, y = split (x2)
    y = int(y)
    if (op == "+"):
        result = (add (x, y))
    elif (op == "-"):
        result = (sub (x, y))
    elif (op == "*"):
        result = (mult (x, y))
    elif (op == "/"):
        result = (div (x, y))
    elif (op == "^"):
        result = (exp (x, y))
        if (y < 0):
            y = -y
            result = 1/exp(x, y)
        elif (y == 0):
            result = 1
    else:
        result = ("!error!")
    return (result)

equ = input ("equation with spaces: ")

print (math (equ))