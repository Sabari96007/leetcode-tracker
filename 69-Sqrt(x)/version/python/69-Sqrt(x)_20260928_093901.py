# Last updated: 28/09/2026, 09:39:01
1class Solution:
2    def mySqrt(self, x):
3        if x < 2:
4            return x
5        left, right, ans = 1, x // 2, 0
6        while left <= right:
7            mid = (left + right) // 2
8            sq = mid * mid
9            if sq == x:
10                return mid
11            if sq < x:
12                ans = mid
13                left = mid + 1
14            else:
15                right = mid - 1
16        return ans
17