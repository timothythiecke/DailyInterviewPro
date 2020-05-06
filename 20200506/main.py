def singleNumber(nums):
  # Fill this in.

    m = {}

    for digit in nums:  
        m[digit] = m.get(digit, 0) + 1 # Auto fill 0 if not exists

    for key in m.keys():
        if m[key] == 1:
            return key

    return -1


'''
    Uses inplace memory of given list to find unique number
    Pre condition: list contains at least 3 elements with one element being unique
'''
def singleNumberOOneSpace(nums): 
    nums.sort()
    for i in range(len(nums)):
        if i > 0 and i < len(nums) - 1: # Some middle element is unique
            if nums[i] != nums[i - 1] and nums[i] != nums[i + 1]:
                return nums[i]
        
        if i == len(nums) - 1: # Final element is unique
            if nums[i] != nums[i - 1]:
                return nums[i]

        if i == 0: # First element is unique
            if nums[i] != nums[i + 1]:
                return nums[i]

    return -1


print (singleNumber([4, 3, 2, 4, 1, 3, 2]))
# 1

print (singleNumberOOneSpace([4, 3, 2, 4, 5, 3, 2, 1, 1])) # 1 1 2 2 3 3 4 4 5
# 5

# Print unique number inside array
# Best idea is to use a map/dictionary, and count the amount of times an element occurs, then look for the element with only 1

# Challenge: use only O(1) memory

'''
Regardless of what you do, you need to iterate over each number in the list
But how can we use O(1) memory, sorting the given list may help
As a unique key requires it to stand out from the other keys
'''