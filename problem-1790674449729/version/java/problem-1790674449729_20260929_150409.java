// Last updated: 29/09/2026, 15:04:09
1class Solution {
2    public int majorityElement(int[] nums) {
3        int candidate = 0, count = 0;
4        for (int num : nums) {
5            if (count == 0) {
6                candidate = num;
7            }
8            count += (num == candidate) ? 1 : -1;
9        }
10        return candidate;
11    }
12}
13