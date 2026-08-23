// LeetCode 0530 - Minimum Absolute Difference in BST
// https://leetcode.com/problems/minimum-absolute-difference-in-bst/

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
    public int GetMinimumDifference(TreeNode root) {
        int best = int.MaxValue;
        int? previous = null;
        Inorder(root, ref previous, ref best);
        return best;
    }

    private static void Inorder(TreeNode node, ref int? previous, ref int best) {
        if (node == null) {
            return;
        }
        Inorder(node.left, ref previous, ref best);
        if (previous.HasValue) {
            best = Math.Min(best, node.val - previous.Value);
        }
        previous = node.val;
        Inorder(node.right, ref previous, ref best);
    }
}
