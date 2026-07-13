// Last updated: 13/07/2026, 09:22:54
1class Solution {
2    public int[] recoverOrder(int[] order, int[] friends) {
3        int[] res = new int[friends.length];
4        int idx = 0;
5        for (int id : order) {
6            for (int f : friends) {
7                if (id == f) {
8                    res[idx++] = id;
9                    break;
10                }
11            }
12        }
13        return res;
14    }
15}
16