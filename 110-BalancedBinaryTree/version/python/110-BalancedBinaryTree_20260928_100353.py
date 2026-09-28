# Last updated: 28/09/2026, 10:03:53
1class TreeNode:
2    def __init__(self, val=0, left=None, right=None):
3        self.val = val
4        self.left = left
5        self.right = right
6
7class Solution:
8    def isBalanced(self, root):
9        def checkHeight(node):
10            if not node:
11                return 0
12            left = checkHeight(node.left)
13            if left == -1:
14                return -1
15            right = checkHeight(node.right)
16            if right == -1:
17                return -1
18            if abs(left - right) > 1:
19                return -1
20            return max(left, right) + 1
21        return checkHeight(root) != -1
22