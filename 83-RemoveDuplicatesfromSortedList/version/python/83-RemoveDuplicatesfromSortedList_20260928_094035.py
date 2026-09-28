# Last updated: 28/09/2026, 09:40:35
1class ListNode:
2    def __init__(self, val=0, next=None):
3        self.val = val
4        self.next = next
5
6class Solution:
7    def deleteDuplicates(self, head):
8        current = head
9        while current and current.next:
10            if current.val == current.next.val:
11                current.next = current.next.next
12            else:
13                current = current.next
14        return head
15