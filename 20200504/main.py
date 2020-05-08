def sortNums(nums):
    # Fill this in.
    # Init amounts
    amounts = [0] * 3
    for num in nums:
        amounts[num - 1] += 1

    # Then loop over the nums list
    i = 0
    j = 0
    while i < len(nums):
        nums[i] = j + 1

        amounts[j] -= 1

        if amounts[j] < 1:
            j += 1

        i += 1
    
    return nums

print(sortNums([3, 3, 2, 1, 3, 2, 1]))
# [1, 1, 2, 2, 3, 3, 3]


# Sort the array containing 1's, 2's and 3's in O(n) time

'''
An approach is to use some variation of count sort
where we keep track of the amount of 1, 2 and 3's in the original array,
after which we fill up the resulting array based on the amounts.
This would mean two loops (1 over the original and 1 over the result) O(2n) -> O(n).
We can return the original list, so we sort in place
'''