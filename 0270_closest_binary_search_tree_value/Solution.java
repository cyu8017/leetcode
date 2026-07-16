// LeetCode 0270 - Closest Binary Search Tree Value
// https://leetcode.com/problems/closest-binary-search-tree-value/

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
    public int closestValue(TreeNode root, double target) {
        int closest = root.val;
        TreeNode current = root;
        while (current != null) {
            if (Math.abs(closest - target) > Math.abs(current.val - target)) {
                closest = current.val;
            }
            if (current.val == target) {
                return current.val;
            }
            current = target < current.val ? current.left : current.right;
        }
        return closest;
    }
}
