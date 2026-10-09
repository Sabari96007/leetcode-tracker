// Last updated: 09/10/2026, 09:12:49
1class Solution {
2    public int minInsertions(String s) {
3        int insertions = 0, open = 0;
4        for (int i = 0; i < s.length(); i++) {
5            char c = s.charAt(i);
6            if (c == '(') {
7                open++;
8            } else {
9                if (i + 1 < s.length() && s.charAt(i + 1) == ')') {
10                    i++;
11                    if (open > 0) open--;
12                    else insertions++;
13                } else {
14                    if (open > 0) {
15                        open--;
16                        insertions++;
17                    } else {
18                        insertions += 2;
19                    }
20                }
21            }
22        }
23        return insertions + open * 2;
24    }
25}
26