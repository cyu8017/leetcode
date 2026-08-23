// LeetCode 0776 - Split BST
// https://leetcode.com/problems/split-bst/

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
    public TreeNode[] splitBST(TreeNode root, int target) {
        if (root == null) return new TreeNode[] {null, null};
        if (root.val <= target) {
            TreeNode[] parts = splitBST(root.right, target);
            root.right = parts[0];
            return new TreeNode[] {root, parts[1]};
        }
        TreeNode[] leftParts = splitBST(root.left, target);
        root.left = leftParts[1];
        return new TreeNode[] {leftParts[0], root};
    }
}
