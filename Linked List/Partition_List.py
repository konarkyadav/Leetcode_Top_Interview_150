# Reference: https://www.youtube.com/watch?v=KT1iUciJr4g&ab_channel=NeetCode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()
        lefttail, righttail = left, right

        while head:
            if head.val < x:
                lefttail.next = head
                lefttail = lefttail.next
            else:
                righttail.next = head
                righttail = righttail.next
            head = head.next
        lefttail.next = right.next
        righttail.next = None
        return left.next