#You are given a positive integer N which represents the number of steps in a staircase. You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.

# Recursive: fn(n - 1)  + fn(n - 2)
# Stop condition: return 1 if n <= 1
def fibonacciRec(n):
    if n <= 1:
        return 1

    return fibonacciRec(n - 1) + fibonacciRec (n - 2)


# Iterative
def fibonacciIt(n):
    i = 1
    
    preprevious = 1
    previous = 2
    
    result = 1
    while i < n:
        if i >= 2:
            result = preprevious + previous
            preprevious = previous
            previous = result 

        i += 1

    return result


def staircase(n):
    # Fill this in.
    #return fibonacciRec(n)
    return fibonacciIt(n)
  
print(staircase(4))
# 5
print(staircase(5))
# 8

print(staircase(7))
# 21
print(staircase(10))
# 89

#Can you find a solution in O(n) time?


# The first thing that springs to mind with the solutions 5 and 8 suggests that it may have something to do with the fibonacci series
# Writing out and testing the different possible cases on a sheet of paper shows that this is indeed the case
# 1 -> 2 -> 3 -> 4 -> 5 -> 6  -> 7
# 1 -> 2 -> 3 -> 5 -> 8 -> 13 -> 21
# Therefore we simply need to implement Fibonacci to solve this problem
# In order to achieve a solution in O(n) time, we can implement Fibonacci iteratively