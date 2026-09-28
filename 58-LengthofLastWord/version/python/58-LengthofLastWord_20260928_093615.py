# Last updated: 28/09/2026, 09:36:15
1class Solution:
2    def lengthOfLastWord(self, s):
3        s = s.strip()
4        return len(s.split()[-1])
5