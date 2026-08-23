// LeetCode 1120 - Maximum Average Subtree
// https://leetcode.com/problems/maximum-average-subtree/

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
var maximumAverageSubtree = function(root) {
    let best = 0;
    const dfs = (node) => {
        if (!node) return [0, 0];
        const [ls, lc] = dfs(node.left);
        const [rs, rc] = dfs(node.right);
        const totalSum = ls + rs + node.val;
        const totalCount = lc + rc + 1;
        best = Math.max(best, totalSum / totalCount);
        return [totalSum, totalCount];
    };
    dfs(root);
    return best;
};
