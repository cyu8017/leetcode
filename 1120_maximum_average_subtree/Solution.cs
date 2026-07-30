// LeetCode 1120 - Maximum Average Subtree
// https://leetcode.com/problems/maximum-average-subtree/

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
    private double best;

    public double MaximumAverageSubtree(TreeNode root) {
        best = 0.0;
        Dfs(root);
        return best;
    }

    private (int sum, int count) Dfs(TreeNode node) {
        if (node == null) {
            return (0, 0);
        }
        var left = Dfs(node.left);
        var right = Dfs(node.right);
        int totalSum = left.sum + right.sum + node.val;
        int totalCount = left.count + right.count + 1;
        best = Math.Max(best, (double)totalSum / totalCount);
        return (totalSum, totalCount);
    }
}
