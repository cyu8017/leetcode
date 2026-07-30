// LeetCode 1339 - Maximum Product Of Splitted Binary Tree
// https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/

using System.Collections.Generic;
public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val; this.left = left; this.right = right;
    }
}

public class Solution {
    public int MaxProduct(TreeNode root) {
        var sums = new List<long>();
        long Total(TreeNode node) {
            if (node == null) return 0;
            long value = node.val + Total(node.left) + Total(node.right);
            sums.Add(value);
            return value;
        }
        long whole = Total(root), best = 0;
        foreach (long value in sums) best = System.Math.Max(best, value * (whole - value));
        return (int)(best % 1000000007);
    }
}
