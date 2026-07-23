# Last updated: 23/07/2026, 10:15:50
1class Solution:
2    def romanToInt(self, s):
3        values = {
4            'I': 1, 'V': 5, 'X': 10,
5            'L': 50, 'C': 100,
6            'D': 500, 'M': 1000
7        }
8        
9        total = 0
10        for i in range(len(s)):
11            if i + 1 < len(s) and values[s[i]] < values[s[i+1]]:
12                total -= values[s[i]]
13            else:
14                total += values[s[i]]
15        return total
16