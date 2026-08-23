// LeetCode 0114 - Flatten Binary Tree to Linked List
// https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

class TreeNode {
    int val; TreeNode left; TreeNode right;
    TreeNode() {}
    TreeNode(int val) { this.val = val; }
    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val; this.left = left; this.right = right;
    }
}

class Solution {
    public void flatten(TreeNode root) {
        flattenTail(root);
    }

    private TreeNode flattenTail(TreeNode node) {
        if (node == null) return null;
        TreeNode leftTail = flattenTail(node.left);
        TreeNode rightTail = flattenTail(node.right);
        if (leftTail != null) {
            leftTail.right = node.right;
            node.right = node.left;
            node.left = null;
        }
        return rightTail != null ? rightTail : (leftTail != null ? leftTail : node);
    }
}