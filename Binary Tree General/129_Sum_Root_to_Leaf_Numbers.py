# Reference: https://www.youtube.com/watch?v=Jk16lZGFWxE&ab_channel=NeetCode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def sumroot(root, summation):
            if not root:
                return 0
            summation = summation*10 + root.val
            if not root.left and not root.right:
                return summation
            return sumroot(root.left, summation) + sumroot(root.right, summation)
        
        return sumroot(root, 0)