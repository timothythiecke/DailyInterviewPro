def singleNumber(nums):
  # Fill this in.

    m = {}

    for digit in nums:  
        m[digit] = m.get(digit, 0) + 1 # Auto fill 0 if not exists

    for key in m.keys():
        if m[key] == 1:
            return key

    return -1

print (singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1


# Print unique number inside array
# Best idea is to use a map/dictionary, and count the amount of times an element occurs, then look for the element with only 1

# Challenge: use only O(1) memory