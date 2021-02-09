#The Fibonacci series
#0, 1, 1, 2, 3, 5, 8, 13, 21, ….
#begins with the terms 0 and 1 and has the property that each succeeding term is the sum of the
#two proceeding terms. Write a function Fibonacci (n) that calculates the nth Fibonacci number.

def Fibonacci(n):
    list=[0,1]
    
    for i in range(2,n+1): 
        list.append(list[i-1]+list[i-2])
    
    print(list[n])
       

Fibonacci(3)

