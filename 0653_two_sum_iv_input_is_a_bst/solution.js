// LeetCode 0653 - Two Sum IV - Input is a BST
// https://leetcode.com/problems/two-sum-iv-input-is-a-bst/

/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {boolean}
 */
var findTarget = function(root, k) {
    const seen = new Set();
    const dfs = (node) => {
        if (node == null) return false;
        if (seen.has(k - node.val)) return true;
        seen.add(node.val);
        return dfs(node.left) || dfs(node.right);
    };
    return dfs(root);
};
