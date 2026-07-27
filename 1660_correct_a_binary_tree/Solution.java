// LeetCode 1660 - Correct a Binary Tree
// https://leetcode.com/problems/correct-a-binary-tree/

import java.util.HashSet;
import java.util.Set;

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
    public TreeNode correctBinaryTree(TreeNode root) {
        Set<TreeNode> seen = new HashSet<>();
        return dfs(root, seen);
    }

    private TreeNode dfs(TreeNode node, Set<TreeNode> seen) {
        if (node == null) {
            return null;
        }
        if (node.right != null && seen.contains(node.right)) {
            return null;
        }
        seen.add(node);
        node.right = dfs(node.right, seen);
        node.left = dfs(node.left, seen);
        return node;
    }
}
