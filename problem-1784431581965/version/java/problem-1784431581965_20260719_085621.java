// Last updated: 19/07/2026, 08:56:21
1/**
2 * Definition for a binary tree node.
3 * public class TreeNode {
4 *     int val;
5 *     TreeNode left;
6 *     TreeNode right;
7 *     TreeNode() {}
8 *     TreeNode(int val) { this.val = val; }
9 *     TreeNode(int val, TreeNode left, TreeNode right) {
10 *         this.val = val;
11 *         this.left = left;
12 *         this.right = right;
13 *     }
14 * }
15 */
16class Solution {
17    private int count = 0; 
18    public int countDominantNodes(TreeNode root) {
19        TreeNode a= root;
20        dfs(a);
21        return count;
22    }
23    private int dfs(TreeNode node){
24        if(node==null) return Integer.MIN_VALUE;
25        int leftMax = dfs(node.left);
26        int rightMax = dfs(node.right);
27
28        int subtreeMax = Math.max(node.val, Math.max(leftMax, rightMax));
29
30        if (node.val == subtreeMax){
31            count++;
32            
33        }
34        return subtreeMax;
35    }
36}