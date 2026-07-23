# Last updated: 23/07/2026, 10:18:52
1class Solution:
2    def longestCommonPrefix(self, strs):
3        if not strs:
4            return ""
5        
6        prefix = strs[0]
7        for s in strs[1:]:
8            while not s.startswith(prefix):
9                prefix = prefix[:-1]
10                if not prefix:
11                    return ""
12        return prefix
13