// LeetCode 2773 - Height of Special Binary Tree
// https://leetcode.com/problems/height-of-special-binary-tree/

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
    public int HeightOfTree(TreeNode root) {
        if (root == null) return -1;
        return Dfs(root);
    }

    private int Dfs(TreeNode node) {
        if (node == null) return -1;
        if (node.left != null && node.left.right == node) return Dfs(node.right) + 1;
        if (node.right != null && node.right.left == node) return Dfs(node.left) + 1;
        return Math.Max(Dfs(node.left), Dfs(node.right)) + 1;
    }
}
