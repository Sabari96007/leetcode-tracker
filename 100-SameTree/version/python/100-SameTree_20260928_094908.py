# Last updated: 28/09/2026, 09:49:08
1class TreeNode:
2    def __init__(self, val=0, left=None, right=None):
3        self.val = val
4        self.left = left
5        self.right = right
6
7class Solution:
8    def isSameTree(self, p, q):
9        if not p and not q:
10            return True
11        if not p or not q:
12            return False
13        if p.val != q.val:
14            return False
15        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
16