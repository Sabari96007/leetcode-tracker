# Last updated: 29/09/2026, 13:59:24
1class TreeNode:
2    def __init__(self, val=0, left=None, right=None):
3        self.val = val
4        self.left = left
5        self.right = right
6
7class Solution:
8    def maxDepth(self, root):
9        if root is None:
10            return 0
11        leftDepth = self.maxDepth(root.left)
12        rightDepth = self.maxDepth(root.right)
13        return 1 + max(leftDepth, rightDepth)
14