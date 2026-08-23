// LeetCode 0776 - Split BST
// https://leetcode.com/problems/split-bst/

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
    public TreeNode[] SplitBST(TreeNode root, int target) {
        if (root == null) return new TreeNode[] { null, null };
        if (root.val <= target) {
            var parts = SplitBST(root.right, target);
            root.right = parts[0];
            return new TreeNode[] { root, parts[1] };
        }
        var leftParts = SplitBST(root.left, target);
        root.left = leftParts[1];
        return new TreeNode[] { leftParts[0], root };
    }
}
