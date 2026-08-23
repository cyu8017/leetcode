// LeetCode 0563 - Binary Tree Tilt
// https://leetcode.com/problems/binary-tree-tilt/

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int val=0, TreeNode left=null, TreeNode right=null) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
public class Solution {
    public int FindTilt(TreeNode root) {
        int total = 0;
        SubtreeSum(root, ref total);
        return total;
    }

    private int SubtreeSum(TreeNode node, ref int total) {
        if (node == null) return 0;
        int left = SubtreeSum(node.left, ref total);
        int right = SubtreeSum(node.right, ref total);
        total += System.Math.Abs(left - right);
        return node.val + left + right;
    }
}
