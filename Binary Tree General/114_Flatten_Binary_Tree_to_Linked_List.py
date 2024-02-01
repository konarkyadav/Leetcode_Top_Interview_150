# Reference: https://www.youtube.com/watch?v=2BdY9fixMrM&ab_channel=CodeHelp-byBabbar

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def flatten(self, root: Optional[TreeNode]) -> None:
#         """
#         Do not return anything, modify root in-place instead.
#         """
#         if not root:
#             return
#         stack = [root]
#         while stack:
#             curr = stack.pop()
#             if curr.right:
#                 stack.append(curr.right)
#             if curr.left:
#                 stack.append(curr.left)
#             if stack:
#                 curr.right = stack[-1]
#             curr.left = None
#         return root      

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        left_tree = self.flatten(root.left)
        right_tree = self.flatten(root.right)
        root.left = None
        root.right = left_tree
        ptr = root
        while ptr.right:
            ptr = ptr.right
        ptr.right = right_tree
        return root