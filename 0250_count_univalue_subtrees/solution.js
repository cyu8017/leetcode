// LeetCode 0250 - Count Univalue Subtrees
// https://leetcode.com/problems/count-univalue-subtrees/

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
var countUnivalSubtrees = function(root) {
    let count = 0;

    const dfs = (node) => {
        if (!node) {
            return true;
        }
        const leftOk = dfs(node.left);
        const rightOk = dfs(node.right);
        if (!leftOk || !rightOk) {
            return false;
        }
        if (node.left && node.left.val !== node.val) {
            return false;
        }
        if (node.right && node.right.val !== node.val) {
            return false;
        }
        count += 1;
        return true;
    };

    dfs(root);
    return count;
};
