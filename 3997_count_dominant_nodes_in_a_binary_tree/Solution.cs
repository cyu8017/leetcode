// LeetCode 3997 - Count Dominant Nodes in a Binary Tree
// https://leetcode.com/problems/count-dominant-nodes-in-a-binary-tree/

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
    int ans = 0;

    int Dfs(TreeNode node) {
        if (node == null) return int.MinValue;
        int l = Dfs(node.left);
        int r = Dfs(node.right);
        int mx = Math.Max(Math.Max(l, r), node.val);
        if (mx == node.val) ans++;
        return mx;
    }

    public int CountDominantNodes(TreeNode root) {
        ans = 0;
        Dfs(root);
        return ans;
    }
}
