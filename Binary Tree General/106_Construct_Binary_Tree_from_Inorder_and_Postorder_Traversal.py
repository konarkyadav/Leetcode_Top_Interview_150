# Reference: https://www.youtube.com/watch?v=vm63HuIU7kw&ab_channel=NeetCodeIO

# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
#         if not inorder:
#             return None
#         root = TreeNode(postorder.pop())
#         mid = inorder.index(root.val)

#         root.right = self.buildTree(inorder[mid+1:], postorder)
#         root.left = self.buildTree(inorder[:mid], postorder)
#         return root

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        inOrderIdx = {v:i for i, v in enumerate(inorder)}
        def helper(l, r):
            if l > r:
                return None
            root = TreeNode(postorder.pop())
            mid = inOrderIdx[root.val]

            root.right = helper(mid+1, r)
            root.left = helper(l, mid-1)
            return root
        return helper(0, len(inorder)-1)