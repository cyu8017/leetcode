// LeetCode 0098 - Validate Binary Search Tree
// https://leetcode.com/problems/validate-binary-search-tree/

function TreeNode(val, left, right) {
    this.val = val === undefined ? 0 : val;
    this.left = left === undefined ? null : left;
    this.right = right === undefined ? null : right;
}

/**
 * @param {TreeNode} root
 * @return {boolean}
 */
var isValidBST = function(root) {
    var valid = function(node, low, high) {
        if (!node) {
            return true;
        }
        if (!(low < node.val && node.val < high)) {
            return false;
        }
        return valid(node.left, low, node.val) && valid(node.right, node.val, high);
    };

    return valid(root, -Infinity, Infinity);
};
