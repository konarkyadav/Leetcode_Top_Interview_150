# Reference: https://www.youtube.com/watch?v=ff6LbGhd1AU&ab_channel=HappyCoding

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        curr = dummy

        while curr:
            # If two nodes are duplicates, move the curr.next forward
            if curr.next and curr.next.next and curr.next.val == curr.next.next.val:
                temp = curr.next.next
                while temp and temp.next and temp.val == temp.next.val:
                    temp = temp.next
                curr.next = temp.next
            else:
                # If the two nodes are not duplicates, move the curr to curr.next
                curr = curr.next
        return dummy.next

