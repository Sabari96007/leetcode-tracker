# Last updated: 28/09/2026, 09:57:11
1
2
3class Solution:
4    def sortedArrayToBST(self, nums):
5        def helper(left, right):
6            if left > right:
7                return None
8            mid = (left + right) // 2
9            root = TreeNode(nums[mid])   
10            root.left = helper(left, mid - 1)
11            root.right = helper(mid + 1, right)
12            return root                  
13        return helper(0, len(nums) - 1)
14