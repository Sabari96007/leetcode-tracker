# Last updated: 29/09/2026, 14:04:06
1class Solution:
2    def isPalindrome(self, s):
3        filtered = ''.join(ch.lower() for ch in s if ch.isalnum())
4        return filtered == filtered[::-1]
5