// LeetCode 1660 - Correct a Binary Tree
// https://leetcode.com/problems/correct-a-binary-tree/

using System.Collections.Generic;

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
    public TreeNode CorrectBinaryTree(TreeNode root) {
        var seen = new HashSet<TreeNode>();
        TreeNode Dfs(TreeNode node) {
            if (node == null) return null;
            if (node.right != null && seen.Contains(node.right)) return null;
            seen.Add(node);
            node.right = Dfs(node.right);
            node.left = Dfs(node.left);
            return node;
        }
        return Dfs(root);
    }
}
