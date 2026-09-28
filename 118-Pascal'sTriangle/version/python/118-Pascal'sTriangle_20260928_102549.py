# Last updated: 28/09/2026, 10:25:49
1class Solution:
2    def generate(self, numRows):
3        triangle = []
4        for i in range(numRows):
5            row = [1] * (i + 1)
6            for j in range(1, i):
7                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
8            triangle.append(row)
9        return triangle
10