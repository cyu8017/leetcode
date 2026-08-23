// LeetCode 0285 - Inorder Successor in BST
// https://leetcode.com/problems/inorder-successor-in-bst/

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
    public TreeNode InorderSuccessor(TreeNode root, TreeNode p) {
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
