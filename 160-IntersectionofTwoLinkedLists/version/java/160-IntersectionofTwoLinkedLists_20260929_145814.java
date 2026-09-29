// Last updated: 29/09/2026, 14:58:14
1public class Solution {
2    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
3        if (headA == null || headB == null) return null;
4        ListNode pA = headA, pB = headB;
5        while (pA != pB) {
6            pA = (pA == null) ? headB : pA.next;
7            pB = (pB == null) ? headA : pB.next;
8        }
9        return pA;
10    }
11}
12