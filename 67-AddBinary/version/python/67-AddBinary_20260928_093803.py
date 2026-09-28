# Last updated: 28/09/2026, 09:38:03
1class Solution:
2    def addBinary(self, a, b):
3        i, j, carry = len(a) - 1, len(b) - 1, 0
4        result = []
5
6        while i >= 0 or j >= 0 or carry:
7            total = carry
8            if i >= 0:
9                total += int(a[i])
10                i -= 1
11            if j >= 0:
12                total += int(b[j])
13                j -= 1
14            result.append(str(total % 2))
15            carry = total // 2
16
17        return ''.join(reversed(result))
18