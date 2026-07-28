// LeetCode 1026 - Maximum Difference Between Node and Ancestor
// https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

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
 * @return {number}
 */
var maxAncestorDiff = function(root) {
    const dfs = (node, lo, hi) => {
        if (!node) return hi - lo;
        lo = Math.min(lo, node.val);
        hi = Math.max(hi, node.val);
        return Math.max(dfs(node.left, lo, hi), dfs(node.right, lo, hi));
    };
    return dfs(root, root.val, root.val);
};
