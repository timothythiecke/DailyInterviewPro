#You are given a positive integer N which represents the number of steps in a staircase. You can either climb 1 or 2 steps at a time. Write a function that returns the number of unique ways to climb the stairs.

def staircase(n):
  # Fill this in.

  
  
print(staircase(4))
# 5
print(staircase(5))
# 8

#Can you find a solution in O(n) time?


# The first thing that springs to mind with the solutions 5 and 8 suggests that it may have something to do with the fibonacci series
# Writing out and testing the different possible cases on a sheet of paper shows that this is indeed the case
# 1 -> 2 -> 3 -> 4 -> 5 -> 6  -> 7
# 1 -> 2 -> 3 -> 5 -> 8 -> 13 -> 21
# Therefore we simply need to implement Fibonacci to solve this problem
# In order to achieve a solution in O(n) time, we can implement Fibonacci iteratively