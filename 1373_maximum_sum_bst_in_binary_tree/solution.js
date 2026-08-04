// LeetCode 1373 - Maximum Sum Bst In Binary Tree
// https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

/**
 * @param {TreeNode} root
 * @return {number}
 */
var maxSumBST = function(root) {
    let ans = 0;
    const dfs = (node) => {
        if (!node) return [true, Infinity, -Infinity, 0];
        const [a, lx, lh, ls] = dfs(node.left);
        const [b, rx, rh, rs] = dfs(node.right);
        if (a && b && lh < node.val && node.val < rx) {
            const s = ls + rs + node.val;
            ans = Math.max(ans, s);
            return [true, Math.min(lx, node.val), Math.max(rh, node.val), s];
        }
        return [false, 0, 0, 0];
    };
    dfs(root);
    return ans;
};
