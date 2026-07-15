// Last updated: 15/07/2026, 09:18:53
1class Solution {
2    public int gcdOfOddEvenSums(int n) {
3        int sumOdd = n * n;          
4        int sumEven = n * (n + 1);    
5        return gcd(sumOdd, sumEven);
6    }
7
8    private int gcd(int a, int b) {
9        while (b != 0) {
10            int temp = a % b;
11            a = b;
12            b = temp;
13        }
14        return a;
15    }
16}
17