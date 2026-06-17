# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = l1
        arr1 = []
        while curr1:
            arr1.append(curr1.val)
            curr1  = curr1.next

        curr2 = l2
        arr2 = []
        while curr2:
            arr2.append(curr2.val)
            curr2  = curr2.next    

        arr1 = arr1[::-1]
        arr2 = arr2[::-1]
        ans = 0

        num1 = int("".join(map(str, arr1))) if arr1 else 0
        num2 = int("".join(map(str, arr2))) if arr2 else 0
        ans = num1 + num2
        
        if ans == 0:
            return ListNode(0)
      
        
        digits = []
        while ans > 0:
            digits.append(ans%10)
            ans = ans // 10
        

        dummy = ListNode(0)
        curr = dummy
        for digit in digits:
            curr.next = ListNode(digit)
            curr = curr.next

        return dummy.next

