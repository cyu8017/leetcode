// LeetCode 0108 - Convert Sorted Array to Binary Search Tree
// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

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
    public TreeNode SortedArrayToBST(int[] nums) {
        return Build(nums, 0, nums.Length - 1);
    }

    private TreeNode Build(int[] nums, int left, int right) {
        if (left > right) {
            return null;
        }
        int mid = (left + right + 1) / 2;
        var root = new TreeNode(nums[mid]);
        root.left = Build(nums, left, mid - 1);
        root.right = Build(nums, mid + 1, right);
        return root;
    }
}
