// LeetCode 1123 - Lowest Common Ancestor of Deepest Leaves
// https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

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
    public TreeNode LcaDeepestLeaves(TreeNode root) {
        return Dfs(root).node;
    }

    private (TreeNode node, int depth) Dfs(TreeNode node) {
        if (node == null) return (null, 0);
        var left = Dfs(node.left);
        var right = Dfs(node.right);
        if (left.depth > right.depth) return (left.node, left.depth + 1);
        if (right.depth > left.depth) return (right.node, right.depth + 1);
        return (node, left.depth + 1);
    }
}
