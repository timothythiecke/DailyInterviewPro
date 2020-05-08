def two_sum(l, k):
    # Fill this in.
    
    m = {}

    for number in l:
        diff = k - number
        
        if number in m:
            return True
        else:
            m[diff] = 0

    return False

print(two_sum([4, 7, 1, -3, 1], -3))
# True

'''
    Try to do it in a single pass of the list

    Return whether the list contains two elements that add up to the given number k
    Condition is that there are two numbers in the list, so a number itself that is equal to k should not count or not yield true
    An idea that springs to mind is to take the difference between k and the number iterated and add it to a dictionary
    If the item exists then you can return true, otherwise add the key to the dict
    Lookup in dict is on average O(1) so very fast (implemented as a hashmap)
'''