# Reference: https://www.youtube.com/watch?v=7v68HVgYXzk&ab_channel=PrakashShukla
# https://www.youtube.com/watch?v=115txA-rS5s&ab_channel=NikhilLohia
# https://www.youtube.com/watch?v=6ZnyEApgFYg&ab_channel=NeetCode

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        if not root:
            return 
        q = deque()
        q.append(root)
        while (q):
            n = len(q)
            total = 0
            for i in range(n):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                total += node.val
            result.append(total/n)
        return result