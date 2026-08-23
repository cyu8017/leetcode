// LeetCode 1676 - Lowest Common Ancestor of a Binary Tree IV
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/

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
    public TreeNode LowestCommonAncestor(TreeNode root, TreeNode[] nodes) {
        var targets = new HashSet<TreeNode>(nodes);
        TreeNode Dfs(TreeNode node) {
            if (node == null) return null;
            var l = Dfs(node.left);
            var r = Dfs(node.right);
            if (targets.Contains(node) || (l != null && r != null)) return node;
            return l ?? r;
        }
        return Dfs(root);
    }
}
