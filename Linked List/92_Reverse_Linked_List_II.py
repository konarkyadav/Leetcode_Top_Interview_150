# Refernce: https://www.youtube.com/watch?v=RF_M9tX4Eag&t=203s&ab_channel=NeetCode

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        leftPrev, cur = dummy, head
        # 1. Reach node at position left
        for i in range(left - 1):
            leftPrev, cur = cur, cur.next
        
        # 2. Now cur = "left", leftPrev = "Node before left"
        # Reverse from left to right
        prev = None
        for i in range(right-left+1):
            tempNext = cur.next
            cur.next = prev
            prev, cur = cur, tempNext
        
        # 3. Update pointers
        leftPrev.next.next = cur #Cur is the node after right
        leftPrev.next = prev # prev is right

        return dummy.next

