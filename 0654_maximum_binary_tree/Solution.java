// LeetCode 0654 - Maximum Binary Tree
// https://leetcode.com/problems/maximum-binary-tree/

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
    private int[] nums;

    public TreeNode constructMaximumBinaryTree(int[] nums) {
        this.nums = nums;
        return build(0, nums.length - 1);
    }

    private TreeNode build(int left, int right) {
        if (left > right) {
            return null;
        }
        int mid = left;
        for (int i = left; i <= right; ++i) {
            if (nums[i] > nums[mid]) {
                mid = i;
            }
        }
        return new TreeNode(nums[mid], build(left, mid - 1), build(mid + 1, right));
    }
}
