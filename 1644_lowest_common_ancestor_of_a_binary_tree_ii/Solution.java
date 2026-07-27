// LeetCode 1644 - Lowest Common Ancestor of a Binary Tree II
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class Solution {
    private int found;

    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        found = 0;
        TreeNode ans = dfs(root, p, q);
        return found == 2 ? ans : null;
    }

    private TreeNode dfs(TreeNode node, TreeNode p, TreeNode q) {
        if (node == null) return null;
        TreeNode left = dfs(node.left, p, q);
        TreeNode right = dfs(node.right, p, q);
        if (node == p || node == q) {
            found++;
            return node;
        }
        if (left != null && right != null) return node;
        return left != null ? left : right;
    }
}
