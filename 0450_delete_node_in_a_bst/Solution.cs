// LeetCode 0450 - Delete Node in a BST
// https://leetcode.com/problems/delete-node-in-a-bst/

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
    public TreeNode DeleteNode(TreeNode root, int key) {
        if (root == null) {
            return null;
        }
        if (key < root.val) {
            root.left = DeleteNode(root.left, key);
        } else if (key > root.val) {
            root.right = DeleteNode(root.right, key);
        } else {
            if (root.left == null) {
                return root.right;
            }
            if (root.right == null) {
                return root.left;
            }
            TreeNode successor = root.right;
            while (successor.left != null) {
                successor = successor.left;
            }
            root.val = successor.val;
            root.right = DeleteNode(root.right, successor.val);
        }
        return root;
    }
}
