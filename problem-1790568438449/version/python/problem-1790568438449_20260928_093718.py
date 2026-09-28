# Last updated: 28/09/2026, 09:37:18
1class Solution:
2    def plusOne(self, digits):
3        for i in range(len(digits) - 1, -1, -1):
4            if digits[i] < 9:
5                digits[i] += 1
6                return digits
7            digits[i] = 0
8        return [1] + digits
9