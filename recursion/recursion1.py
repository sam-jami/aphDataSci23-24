#can only look at chars one/time
n = 6

def add (n):
    #base case
    if (n == 1):
       return 1
    #recursion
    else: 
        return add(n-1) + n
    
print (add (n))