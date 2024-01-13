# Reference: https://www.youtube.com/watch?v=RtU1BtAfKB8&ab_channel=ErraK

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.min_diff = float('Inf')
        self.prev_val = None

        def dfs(root):
            if root is None:
                return
            dfs(root.left)

            if self.prev_val is not None:
                self.min_diff = min(self.min_diff, abs(root.val - self.prev_val))
            self.prev_val = root.val

            dfs(root.right)
        
        dfs(root)
        return self.min_diff