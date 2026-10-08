// Last updated: 08/10/2026, 09:21:55
1class Solution {
2    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
3        ListNode dummy = new ListNode(0);
4        ListNode current = dummy;
5        int carry = 0;
6
7        while (l1 != null || l2 != null || carry != 0) {
8            int sum = carry;
9            if (l1 != null) {
10                sum += l1.val;
11                l1 = l1.next;
12            }
13            if (l2 != null) {
14                sum += l2.val;
15                l2 = l2.next;
16            }
17            carry = sum / 10;
18            current.next = new ListNode(sum % 10);
19            current = current.next;
20        }
21        return dummy.next;
22    }
23}
24