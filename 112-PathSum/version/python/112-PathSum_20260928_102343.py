# Last updated: 28/09/2026, 10:23:43
1class Solution:
2    def hasPathSum(self, root, targetSum):
3        if not root:
4            return False
5        if not root.left and not root.right:
6            return targetSum == root.val
7        return (self.hasPathSum(root.left, targetSum - root.val) or
8                self.hasPathSum(root.right, targetSum - root.val))
9