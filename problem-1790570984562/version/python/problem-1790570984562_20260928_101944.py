# Last updated: 28/09/2026, 10:19:44
1class Solution:
2    def minDepth(self, root):
3        if not root:
4            return 0
5        
6        if not root.left:
7            return 1 + self.minDepth(root.right)
8        if not root.right:
9            return 1 + self.minDepth(root.left)
10        
11        return 1 + min(self.minDepth(root.left), self.minDepth(root.right))
12