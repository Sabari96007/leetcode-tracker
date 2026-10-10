// Last updated: 10/10/2026, 12:05:55
1class Solution {
2    public int maxArea(int[] height) {
3        int left = 0, right = height.length - 1;
4        int maxArea = 0;
5        
6        while (left < right) {
7            int width = right - left;
8            int h = Math.min(height[left], height[right]);
9            int area = width * h;
10            maxArea = Math.max(maxArea, area);
11            
12            if (height[left] < height[right]) {
13                left++;
14            } else {
15                right--;
16            }
17        }
18        
19        return maxArea;
20    }
21}
22