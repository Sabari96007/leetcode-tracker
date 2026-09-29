// Last updated: 29/09/2026, 14:55:50
1import java.util.*;
2
3class Solution {
4    public List<Integer> postorderTraversal(TreeNode root) {
5        List<Integer> result = new ArrayList<>();
6        postorder(root, result);
7        return result;
8    }
9
10    private void postorder(TreeNode node, List<Integer> result) {
11        if (node == null) return;
12        postorder(node.left, result);
13        postorder(node.right, result);
14        result.add(node.val);
15    }
16}
17