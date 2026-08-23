// LeetCode 0101 - Symmetric Tree
// https://leetcode.com/problems/symmetric-tree/

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
    public bool IsSymmetric(TreeNode root) {
        if (root == null) {
            return true;
        }
        return Mirrors(root.left, root.right);
    }

    private bool Mirrors(TreeNode left, TreeNode right) {
        if (left == null && right == null) {
            return true;
        }
        if (left == null || right == null || left.val != right.val) {
            return false;
        }
        return Mirrors(left.left, right.right) && Mirrors(left.right, right.left);
    }
}
