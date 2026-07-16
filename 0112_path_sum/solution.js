// LeetCode 0112 - Path Sum
// https://leetcode.com/problems/path-sum/

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

/**
 * @param {TreeNode} root
 * @param {number} targetSum
 * @return {boolean}
 */
var hasPathSum = function(root, targetSum) {
    if (!root) {
        return false;
    }
    if (!root.left && !root.right) {
        return root.val === targetSum;
    }
    return hasPathSum(root.left, targetSum - root.val) ||
        hasPathSum(root.right, targetSum - root.val);
};