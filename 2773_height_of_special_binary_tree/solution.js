// LeetCode 2773 - Height of Special Binary Tree
// https://leetcode.com/problems/height-of-special-binary-tree/

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
 * @return {number}
 */
var heightOfTree = function(root) {
    if (!root) return -1;
    const dfs = (node) => {
        if (!node) return -1;
        if (node.left && node.left.right === node) return dfs(node.right) + 1;
        if (node.right && node.right.left === node) return dfs(node.left) + 1;
        return Math.max(dfs(node.left), dfs(node.right)) + 1;
    };
    return dfs(root);
};
