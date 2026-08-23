// LeetCode 0654 - Maximum Binary Tree
// https://leetcode.com/problems/maximum-binary-tree/

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
    private int[] nums;

    public TreeNode ConstructMaximumBinaryTree(int[] nums) {
        this.nums = nums;
        return Build(0, nums.Length - 1);
    }

    private TreeNode Build(int left, int right) {
        if (left > right) return null;
        int mid = left;
        for (int i = left; i <= right; ++i) {
            if (nums[i] > nums[mid]) mid = i;
        }
        return new TreeNode(nums[mid], Build(left, mid - 1), Build(mid + 1, right));
    }
}
