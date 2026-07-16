// LeetCode 0129 - Sum Root to Leaf Numbers
// https://leetcode.com/problems/sum-root-to-leaf-numbers/

/**
 * Definition for a binary tree node.
 * @param {number} [val]
 * @param {TreeNode|null} [left]
 * @param {TreeNode|null} [right]
 */
function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

/**
 * @param {TreeNode|null} root
 * @return {number}
 */
var sumNumbers = function(root) {
    const dfs = (node, current) => {
        if (!node) {
            return 0;
        }

        const value = current * 10 + node.val;
        if (!node.left && !node.right) {
            return value;
        }
        return dfs(node.left, value) + dfs(node.right, value);
    };

    return dfs(root, 0);
};