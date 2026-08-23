// LeetCode 0993 - Cousins in Binary Tree
// https://leetcode.com/problems/cousins-in-binary-tree/

import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val; this.left = left; this.right = right;
    }
}

class Solution {
    private final Map<Integer, Integer> depth = new HashMap<>();
    private final Map<Integer, TreeNode> parent = new HashMap<>();

    public boolean isCousins(TreeNode root, int x, int y) {
        depth.clear();
        parent.clear();
        dfs(root, null, 0);
        return depth.get(x).equals(depth.get(y)) && parent.get(x) != parent.get(y);
    }

    private void dfs(TreeNode node, TreeNode p, int d) {
        if (node == null) return;
        depth.put(node.val, d);
        parent.put(node.val, p);
        dfs(node.left, node, d + 1);
        dfs(node.right, node, d + 1);
    }
}
