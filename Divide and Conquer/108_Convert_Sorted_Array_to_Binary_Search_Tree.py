# Reference: https://www.youtube.com/watch?v=0K0uCMYq5ng&ab_channel=NeetCode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def createTree(left, right):
            if left > right:
                return None
            m = (left + right) // 2
            return TreeNode(nums[m], createTree(left, m-1), createTree(m+1, right))
        
        return createTree(0, len(nums)-1)