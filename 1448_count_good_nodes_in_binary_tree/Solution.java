// LeetCode 1448 - Count Good Nodes In Binary Tree
// https://leetcode.com/problems/count-good-nodes-in-binary-tree/

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
    public int goodNodes(TreeNode root) {
        return dfs(root, Integer.MIN_VALUE);
    }

    private int dfs(TreeNode node, int maxSoFar) {
        if (node == null) return 0;
        int add = node.val >= maxSoFar ? 1 : 0;
        int next = Math.max(maxSoFar, node.val);
        return add + dfs(node.left, next) + dfs(node.right, next);
    }
}
