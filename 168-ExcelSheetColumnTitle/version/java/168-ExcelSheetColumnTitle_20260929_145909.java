// Last updated: 29/09/2026, 14:59:09
1class Solution {
2    public String convertToTitle(int columnNumber) {
3        StringBuilder sb = new StringBuilder();
4        while (columnNumber > 0) {
5            columnNumber--; 
6            sb.append((char) ('A' + (columnNumber % 26)));
7            columnNumber /= 26;
8        }
9        return sb.reverse().toString();
10    }
11}
12