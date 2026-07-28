// LeetCode 1026 - Maximum Difference Between Node and Ancestor
// https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

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
    public int maxAncestorDiff(TreeNode root) {
        return dfs(root, root.val, root.val);
    }

    private int dfs(TreeNode node, int lo, int hi) {
        if (node == null) return hi - lo;
        lo = Math.min(lo, node.val);
        hi = Math.max(hi, node.val);
        return Math.max(dfs(node.left, lo, hi), dfs(node.right, lo, hi));
    }
}
