// LeetCode 0426 - Convert Binary Search Tree to Sorted Doubly Linked List
// https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/

public class TreeNode {
    public int val;
    public TreeNode left;
    public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val;
        this.left = left;
        this.right = right;
    }
}

public class Solution {
    public TreeNode TreeToDoublyList(TreeNode root) {
        if (root == null) {
            return null;
        }

        TreeNode first = null;
        TreeNode last = null;

        void Inorder(TreeNode node) {
            if (node == null) {
                return;
            }
            Inorder(node.left);
            if (last != null) {
                last.right = node;
                node.left = last;
            } else {
                first = node;
            }
            last = node;
            Inorder(node.right);
        }

        Inorder(root);
        if (first != null && last != null) {
            first.left = last;
            last.right = first;
        }
        return first;
    }
}
