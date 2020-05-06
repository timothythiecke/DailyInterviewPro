# Definition for singly-linked list.
class ListNode(object):
  def __init__(self, x):
    self.val = x
    self.next = None

class Solution:
  def addTwoNumbers(self, l1, l2, c = 0): # I assume the c is used as a carry
    # Fill this in.
    # Function will return a linked list (solution in this case is 7 - 0 - 8)

    result = ListNode(0)
    driver_main = result # Used to create the linked list

    while l1 and l2:        
        summation = l1.val + l2.val
        modulo = summation % 10
        driver_main.val = modulo + c

        c = int(summation / 10)

        # In case of carry overflow
        if driver_main.val > 9:
            c = c + int(driver_main.val / 10)
            driver_main.val = driver_main.val % 10

        # Continue to the next part
        l1 = l1.next
        l2 = l2.next

        if (l1 and l2) or c > 0:
            driver_main.next = ListNode(0)
            driver_main = driver_main.next
            
            if c > 0:
                driver_main.val = c

    return result




'''l1 = ListNode(2)
l1.next = ListNode(4)
l1.next.next = ListNode(3)

l2 = ListNode(5)
l2.next = ListNode(6)
l2.next.next = ListNode(4)
'''

l1 = ListNode(1)
l1.next = ListNode(1)
l1.next.next = ListNode(1)

l2 = ListNode(9)
l2.next = ListNode(9)
l2.next.next = ListNode(9)
#'''

result = Solution().addTwoNumbers(l1, l2)
while result:
  print (result.val, end=' ')
  result = result.next
# 7 0 8