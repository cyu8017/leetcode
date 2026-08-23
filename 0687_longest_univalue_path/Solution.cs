// LeetCode 0687 - Longest Univalue Path
// https://leetcode.com/problems/longest-univalue-path/

using System;

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}
public class Solution {
    private int best;

    private int Dfs(TreeNode node) {
        if (node == null) return 0;
        int left = Dfs(node.left);
        int right = Dfs(node.right);
        int leftPath = node.left != null && node.left.val == node.val ? left + 1 : 0;
        int rightPath = node.right != null && node.right.val == node.val ? right + 1 : 0;
        best = Math.Max(best, leftPath + rightPath);
        return Math.Max(leftPath, rightPath);
    }

    public int LongestUnivaluePath(TreeNode root) {
        best = 0;
        Dfs(root);
        return best;
    }
}
