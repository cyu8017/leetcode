// LeetCode 2792 - Count Nodes That Are Great Enough
// https://leetcode.com/problems/count-nodes-that-are-great-enough/

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
 * @return {number}
 */
var countGreatEnoughNodes = function(root, k) {
    let ans = 0;
    const dfs = (node) => {
        if (!node) return [];
        const vals = [node.val, ...dfs(node.left), ...dfs(node.right)];
        let smaller = 0;
        for (const v of vals) if (v < node.val) smaller++;
        if (smaller >= k) ans++;
        return vals;
    };
    dfs(root);
    return ans;
};
