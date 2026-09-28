# Last updated: 28/09/2026, 09:30:05
1class Solution:
2    def isValid(self, s):
3        stack = []
4        mapping = {')': '(', '}': '{', ']': '['}
5        for char in s:
6            if char in mapping.values():
7                stack.append(char)
8            elif char in mapping:
9                if not stack or stack.pop() != mapping[char]:
10                    return False
11        return not stack
12