// LeetCode 0124 - Binary Tree Maximum Path Sum
// https://leetcode.com/problems/binary-tree-maximum-path-sum/

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

    public int MaxPathSum(TreeNode root) {
        best = int.MinValue;
        Gain(root);
        return best;
    }

    private int Gain(TreeNode node) {
        if (node == null) return 0;
        int left = System.Math.Max(Gain(node.left), 0);
        int right = System.Math.Max(Gain(node.right), 0);
        best = System.Math.Max(best, node.val + left + right);
        return node.val + System.Math.Max(left, right);
    }
}