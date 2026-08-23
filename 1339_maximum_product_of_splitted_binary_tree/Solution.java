// LeetCode 1339 - Maximum Product Of Splitted Binary Tree
// https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

import java.util.*;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    private List<Long> sums = new ArrayList<>();

    public int maxProduct(TreeNode root) {
        long whole = total(root);
        long best = 0;
        for (long value : sums) best = Math.max(best, value * (whole - value));
        return (int) (best % 1_000_000_007);
    }

    private long total(TreeNode node) {
        if (node == null) return 0;
        long value = node.val + total(node.left) + total(node.right);
        sums.add(value);
        return value;
    }
}
