// LeetCode 0108 - Convert Sorted Array to Binary Search Tree
// https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

/**
 * @param {number[]} nums
 * @return {TreeNode}
 */
var sortedArrayToBST = function(nums) {
    function build(left, right) {
        if (left > right) {
            return null;
        }
        var mid = Math.floor((left + right + 1) / 2);
        var root = new TreeNode(nums[mid]);
        root.left = build(left, mid - 1);
        root.right = build(mid + 1, right);
        return root;
    }
    return build(0, nums.length - 1);
};
