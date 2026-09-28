# Last updated: 28/09/2026, 09:39:54
1class Solution:
2    def climbStairs(self, n):
3        if n <= 2:
4            return n
5        a, b = 1, 2
6        for i in range(3, n + 1):
7            a, b = b, a + b
8        return b
9