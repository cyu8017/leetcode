// LeetCode 0426 - Convert Binary Search Tree to Sorted Doubly Linked List
// https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

class TreeNode {
    int val;
    TreeNode left;
    TreeNode right;

    TreeNode() {}

    TreeNode(int val) {
        this.val = val;
    }

    TreeNode(int val, TreeNode left, TreeNode right) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

class Solution {
    private TreeNode first;
    private TreeNode last;

    public TreeNode treeToDoublyList(TreeNode root) {
        if (root == null) {
            return null;
        }

        first = null;
        last = null;
        inorder(root);
        first.left = last;
        last.right = first;
        return first;
    }

    private void inorder(TreeNode node) {
        if (node == null) {
            return;
        }
        inorder(node.left);
        if (last != null) {
            last.right = node;
            node.left = last;
        } else {
            first = node;
        }
        last = node;
        inorder(node.right);
    }
}
