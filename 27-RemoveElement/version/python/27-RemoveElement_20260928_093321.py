# Last updated: 28/09/2026, 09:33:21
1class Solution:
2    def removeElement(self, nums, val):
3        k = 0
4        for i in range(len(nums)):
5            if nums[i] != val:
6                nums[k] = nums[i]
7                k += 1
8        return k
9