# Last updated: 28/09/2026, 09:31:32
1class ListNode:
2    def __init__(self, val=0, next=None):
3        self.val = val
4        self.next = next
5
6class Solution:
7    def mergeTwoLists(self, list1, list2):
8        dummy = ListNode(-1)
9        current = dummy
10
11        while list1 and list2:
12            if list1.val <= list2.val:
13                current.next = list1
14                list1 = list1.next
15            else:
16                current.next = list2
17                list2 = list2.next
18            current = current.next
19
20        current.next = list1 if list1 else list2
21        return dummy.next
22