// Last updated: 09/10/2026, 09:18:34
1class Solution {
2    public int minMoves(int[] nums, int limit) {
3        int n = nums.length;
4        int[] diff = new int[2 * limit + 2];
5
6        for (int i = 0; i < n / 2; i++) {
7            int a = nums[i], b = nums[n - 1 - i];
8            int low = Math.min(a, b) + 1;
9            int high = Math.max(a, b) + limit;
10            int sum = a + b;
11
12            diff[2] += 2;
13            diff[low] -= 1;
14            diff[sum] -= 1;
15            diff[sum + 1] += 1;
16            diff[high + 1] += 1;
17        }
18
19        int res = Integer.MAX_VALUE, curr = 0;
20        for (int i = 2; i <= 2 * limit; i++) {
21            curr += diff[i];
22            res = Math.min(res, curr);
23        }
24        return res;
25    }
26}
27