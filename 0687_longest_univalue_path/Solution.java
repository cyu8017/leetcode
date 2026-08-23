// LeetCode 0687 - Longest Univalue Path
// https://leetcode.com/problems/longest-univalue-path/

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
    private int best;

    private int dfs(TreeNode node) {
        if (node == null) return 0;
        int left = dfs(node.left);
        int right = dfs(node.right);
        int leftPath = node.left != null && node.left.val == node.val ? left + 1 : 0;
        int rightPath = node.right != null && node.right.val == node.val ? right + 1 : 0;
        best = Math.max(best, leftPath + rightPath);
        return Math.max(leftPath, rightPath);
    }

    public int longestUnivaluePath(TreeNode root) {
        best = 0;
        dfs(root);
        return best;
    }
}
