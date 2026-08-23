// LeetCode 0112 - Path Sum
// https://leetcode.com/problems/path-sum/

public class Solution {
    public bool HasPathSum(TreeNode root, int targetSum) {
        if (root == null) return false;
        if (root.left == null && root.right == null) return root.val == targetSum;
        return HasPathSum(root.left, targetSum - root.val)
            || HasPathSum(root.right, targetSum - root.val);
    }
}

public class TreeNode {
    public int val; public TreeNode left; public TreeNode right;
    public TreeNode(int val = 0, TreeNode left = null, TreeNode right = null) {
        this.val = val; this.left = left; this.right = right;
    }
}