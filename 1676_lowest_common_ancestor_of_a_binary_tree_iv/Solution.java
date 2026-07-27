// LeetCode 1676 - Lowest Common Ancestor of a Binary Tree IV
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/

import java.util.HashSet;
import java.util.Set;

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;
    TreeNode(int x) { val = x; }
}

class Solution {
    public TreeNode lowestCommonAncestor(TreeNode root, TreeNode[] nodes) {
        Set<TreeNode> targets = new HashSet<>();
        for (TreeNode node : nodes) {
            targets.add(node);
        }
        return dfs(root, targets);
    }

    private TreeNode dfs(TreeNode node, Set<TreeNode> targets) {
        if (node == null) {
            return null;
        }
        TreeNode left = dfs(node.left, targets);
        TreeNode right = dfs(node.right, targets);
        if (targets.contains(node) || (left != null && right != null)) {
            return node;
        }
        return left != null ? left : right;
    }
}
