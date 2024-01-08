import random

"""for i in range(8):
    #creates an empty list and then fills it with random values
    list[i] = random.randint(1, 50)"""

# IMPLEMENT ALL OF THESE FUNCTIONS

thelist = [32, 3, 2, 3, 2, 4, 5, 2, 4]
v = 2

def sumList(thelist):
    # returns the sum of the integers in list thelist.

    if (len(thelist) == 1):
        return thelist[0]
    elif (len(thelist) == 0):
        return 0
    return thelist[0] + sumList (thelist[1:]) # Stub return.  Replace this.

def numberOf(thelist, v):    
    #returns the number of times v occurs in thelist.
    if (len(thelist) == 0):
        return 0
    if (thelist[0] == v):
        return numberOf (thelist[1:], v) + 1
    else:
        return numberOf (thelist[1:], v)

def numberNot(thelist, v):
    #Returns the number of elements in thelist that are NOT v.
    
    if (len(thelist) == 0):
        return 0
    return len(thelist) - numberOf(thelist, v) # Stub return.  Replace this.

def removeFirst(thelist, v):
    """
    Returns a COPY of thelist but with the FIRST occurrence of v removed (if present).

    Note: This can be done easily using the method index. Don't do that.
    Do it recursively.

    Parameter thelist: the list to search
    Precondition: thelist is a list of ints

    Parameter v: the value to search for
    Precondition: v is an int
    """
    return [] # Stub return.  Replace this.
