# Last updated: 28/09/2026, 09:51:23
1class TreeNode:
2    def __init__(self, val=0, left=None, right=None):
3        self.val = val
4        self.left = left
5        self.right = right
6
7class Solution:
8    def isSymmetric(self, root):
9        if not root:
10            return True
11
12        def isMirror(t1, t2):
13            if not t1 and not t2:
14                return True
15            if not t1 or not t2:
16                return False
17            return (t1.val == t2.val and
18                    isMirror(t1.left, t2.right) and
19                    isMirror(t1.right, t2.left))
20
21        return isMirror(root.left, root.right)
22