// LeetCode 1123 - Lowest Common Ancestor of Deepest Leaves
// https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    public TreeNode lcaDeepestLeaves(TreeNode root) {
        return dfs(root).node;
    }

    private static class Result {
        TreeNode node;
        int depth;
        Result(TreeNode node, int depth) {
            this.node = node;
            this.depth = depth;
        }
    }

    private Result dfs(TreeNode node) {
        if (node == null) return new Result(null, 0);
        Result left = dfs(node.left);
        Result right = dfs(node.right);
        if (left.depth > right.depth) return new Result(left.node, left.depth + 1);
        if (right.depth > left.depth) return new Result(right.node, right.depth + 1);
        return new Result(node, left.depth + 1);
    }
}
