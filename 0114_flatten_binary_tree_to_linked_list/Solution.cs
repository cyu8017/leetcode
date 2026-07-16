// LeetCode 0114 - Flatten Binary Tree to Linked List
// https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

public class TreeNode {
    public int val; public TreeNode left; public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val; this.left = left; this.right = right;
    }
}

public class Solution {
    public void Flatten(TreeNode root) {
        FlattenTail(root);
    }

    private TreeNode FlattenTail(TreeNode node) {
        if (node == null) return null;
        TreeNode leftTail = FlattenTail(node.left);
        TreeNode rightTail = FlattenTail(node.right);
        if (leftTail != null) {
            leftTail.right = node.right;
            node.right = node.left;
            node.left = null;
        }
        return rightTail ?? leftTail ?? node;
    }
}