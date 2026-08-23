// LeetCode 0701 - Insert into a Binary Search Tree
// https://leetcode.com/problems/insert-into-a-binary-search-tree/

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
    public TreeNode insertIntoBST(TreeNode root, int val) {
        if (root == null) return new TreeNode(val);
        TreeNode node = root;
        while (true) {
            if (val < node.val) {
                if (node.left == null) { node.left = new TreeNode(val); break; }
                node = node.left;
            } else {
                if (node.right == null) { node.right = new TreeNode(val); break; }
                node = node.right;
            }
        }
        return root;
    }
}
