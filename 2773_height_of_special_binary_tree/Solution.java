// LeetCode 2773 - Height of Special Binary Tree
// https://leetcode.com/problems/height-of-special-binary-tree/

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
    public int heightOfTree(TreeNode root) {
        if (root == null) return -1;
        return dfs(root);
    }

    private int dfs(TreeNode node) {
        if (node == null) return -1;
        if (node.left != null && node.left.right == node) return dfs(node.right) + 1;
        if (node.right != null && node.right.left == node) return dfs(node.left) + 1;
        return Math.max(dfs(node.left), dfs(node.right)) + 1;
    }
}
