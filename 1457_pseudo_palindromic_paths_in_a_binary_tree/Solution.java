// LeetCode 1457 - Pseudo Palindromic Paths In A Binary Tree
// https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

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
    public int pseudoPalindromicPaths(TreeNode root) {
        return dfs(root, 0);
    }

    private int dfs(TreeNode node, int mask) {
        if (node == null) return 0;
        mask ^= 1 << node.val;
        if (node.left == null && node.right == null) {
            return (mask & (mask - 1)) == 0 ? 1 : 0;
        }
        return dfs(node.left, mask) + dfs(node.right, mask);
    }
}
