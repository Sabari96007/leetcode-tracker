# Last updated: 03/09/2026, 09:31:06
1class Solution:
2    def concatWithReverse(self, nums):
3        n = len(nums)
4        ans = [0] * (2 * n)
5        for i in range(n):
6            ans[i] = nums[i]
7        for i in range(n):
8            ans[i + n] = nums[n - i - 1]
9        return ans
10