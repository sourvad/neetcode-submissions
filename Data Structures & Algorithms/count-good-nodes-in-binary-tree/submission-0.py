# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(node, maxSoFar):
            if not node:
                return 0
            
            goodNodes = 0

            if node.val >= maxSoFar:
                goodNodes += 1
                maxSoFar = node.val

            goodNodes += dfs(node.left, maxSoFar)
            goodNodes += dfs(node.right, maxSoFar)

            return goodNodes


        return dfs(root, root.val)
