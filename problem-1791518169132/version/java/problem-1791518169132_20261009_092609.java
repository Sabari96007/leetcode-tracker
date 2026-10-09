// Last updated: 09/10/2026, 09:26:09
1class Solution {
2    public boolean isGood(int[] nums) {
3        int n = nums.length;
4        int max = 0;
5        for (int num : nums) max = Math.max(max, num);
6        if (max != n - 1) return false;
7
8        int[] count = new int[n];
9        for (int num : nums) {
10            if (num > n - 1) return false;
11            count[num - 1]++;
12        }
13
14        for (int i = 0; i < n - 2; i++) {
15            if (count[i] != 1) return false;
16        }
17        return count[n - 2] == 2;
18    }
19}
20