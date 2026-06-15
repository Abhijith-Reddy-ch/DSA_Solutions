# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from collections import deque
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1: return list2
        if not list2: return list1
        
        curr1 = list1
        curr2 = list2
        queue = deque()

        while curr1 and curr2:
            if curr1.val>curr2.val:
                queue.append(curr2.val)
                curr2 = curr2.next
            else:
                queue.append(curr1.val)
                curr1 = curr1.next

        
        while curr1:
            queue.append(curr1.val)
            curr1 = curr1.next
        while curr2:
            queue.append(curr2.val)
            curr2 = curr2.next
        
        
        dummy = ListNode(0)
        curr = dummy
        while queue:
            curr.next = ListNode(queue.popleft())
            curr = curr.next
        
        return dummy.next

