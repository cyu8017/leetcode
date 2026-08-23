// LeetCode 0285 - Inorder Successor in BST
// https://leetcode.com/problems/inorder-successor-in-bst/

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
    public TreeNode inorderSuccessor(TreeNode root, TreeNode p) {
        if (p.right != null) {
            TreeNode current = p.right;
            while (current.left != null) {
                current = current.left;
            }
            return current;
        }

        TreeNode successor = null;
        TreeNode current = root;
        while (current != null) {
            if (p.val < current.val) {
                successor = current;
                current = current.left;
            } else {
                current = current.right;
            }
        }
        return successor;
    }
}
