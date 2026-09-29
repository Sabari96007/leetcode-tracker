// Last updated: 29/09/2026, 14:12:10
1import java.util.*;
2
3class Solution {
4    public List<Integer> preorderTraversal(TreeNode root) {
5        List<Integer> result = new ArrayList<>();
6        preorder(root, result);
7        return result;
8    }
9
10    private void preorder(TreeNode node, List<Integer> result) {
11        if (node == null) return;
12        result.add(node.val);
13        preorder(node.left, result);
14        preorder(node.right, result);
15    }
16}
17