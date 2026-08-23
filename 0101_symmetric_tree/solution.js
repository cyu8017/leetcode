// LeetCode 0101 - Symmetric Tree
// https://leetcode.com/problems/symmetric-tree/

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
 * @param {TreeNode} root
 * @return {boolean}
 */
var isSymmetric = function(root) {
    if (!root) {
        return true;
    }

    var mirrors = function(left, right) {
        if (!left && !right) {
            return true;
        }
        if (!left || !right || left.val !== right.val) {
            return false;
        }
        return mirrors(left.left, right.right) && mirrors(left.right, right.left);
    };

    return mirrors(root.left, root.right);
};
