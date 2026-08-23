// LeetCode 0654 - Maximum Binary Tree
// https://leetcode.com/problems/maximum-binary-tree/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var constructMaximumBinaryTree = function(nums) {
    const build = (left, right) => {
        if (left > right) return null;
        let mid = left;
        for (let i = left; i <= right; ++i) if (nums[i] > nums[mid]) mid = i;
        return new TreeNode(nums[mid], build(left, mid - 1), build(mid + 1, right));
    };
    return build(0, nums.length - 1);
};
