n = 10

def fibonacci (n):
    #base case
    if (n == 1 or n == 2):
       return 1
    #recursion
    else: 
        return fibonacci(n-1) + fibonacci(n-2)
    
print (fibonacci (n))
