# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []
        curr = head
        while curr:
            stack.append(curr)
            curr = curr.next
        
        curr = head
        n = len(stack)
        for i in range(n//2):
            last_node = stack[n-1-i]
            next_node = curr.next
            curr.next = last_node
            last_node.next = next_node

            curr = next_node
        
        curr.next = None
        

