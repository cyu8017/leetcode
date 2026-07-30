// LeetCode 1457 - Pseudo Palindromic Paths In A Binary Tree
// https://leetcode.com/problems/pseudo-palindromic-paths-in-a-binary-tree/

public class TreeNode {
    public int val; public TreeNode left; public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val; this.left = left; this.right = right;
    }
}
public class Solution {
    public int PseudoPalindromicPaths(TreeNode root) {
        int Dfs(TreeNode node, int mask) {
            if (node == null) return 0;
            mask ^= 1 << node.val;
            if (node.left == null && node.right == null) return (mask & (mask - 1)) == 0 ? 1 : 0;
            return Dfs(node.left, mask) + Dfs(node.right, mask);
        }
        return Dfs(root, 0);
    }
}
