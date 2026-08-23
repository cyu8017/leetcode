// LeetCode 0563 - Binary Tree Tilt
// https://leetcode.com/problems/binary-tree-tilt/

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
    private int total;

    public int findTilt(TreeNode root) {
        total = 0;
        subtreeSum(root);
        return total;
    }

    private int subtreeSum(TreeNode node) {
        if (node == null) {
            return 0;
        }
        int left = subtreeSum(node.left);
        int right = subtreeSum(node.right);
        total += Math.abs(left - right);
        return node.val + left + right;
    }
}
