// LeetCode 0270 - Closest Binary Search Tree Value
// https://leetcode.com/problems/closest-binary-search-tree-value/

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
    public int ClosestValue(TreeNode root, double target) {
        int closest = root.val;
        TreeNode current = root;
        while (current != null) {
            if (System.Math.Abs(closest - target) > System.Math.Abs(current.val - target)) {
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
