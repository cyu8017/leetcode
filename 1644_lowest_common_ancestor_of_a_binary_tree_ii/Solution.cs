// LeetCode 1644 - Lowest Common Ancestor of a Binary Tree II
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int x) { val = x; }
}

public class Solution {
    private int found;

    public TreeNode LowestCommonAncestor(TreeNode root, TreeNode p, TreeNode q) {
        found = 0;
        var ans = Dfs(root, p, q);
        return found == 2 ? ans : null;
    }

    private TreeNode Dfs(TreeNode node, TreeNode p, TreeNode q) {
        if (node == null) return null;
        var left = Dfs(node.left, p, q);
        var right = Dfs(node.right, p, q);
        if (node == p || node == q) {
            found++;
            return node;
        }
        if (left != null && right != null) return node;
        return left ?? right;
    }
}
