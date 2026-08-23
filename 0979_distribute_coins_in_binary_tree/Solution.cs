// LeetCode 0979 - Distribute Coins in Binary Tree
// https://leetcode.com/problems/distribute-coins-in-binary-tree/

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
    public int DistributeCoins(TreeNode root) {
        int ans = 0;
        int Dfs(TreeNode node) {
            if (node == null) return 0;
            int left = Dfs(node.left);
            int right = Dfs(node.right);
            ans += Math.Abs(left) + Math.Abs(right);
            return node.val + left + right - 1;
        }
        Dfs(root);
        return ans;
    }
}
