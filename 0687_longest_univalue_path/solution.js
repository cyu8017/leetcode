// LeetCode 0687 - Longest Univalue Path
// https://leetcode.com/problems/longest-univalue-path/

/**
 * @param {TreeNode} root
 * @return {number}
 */
var longestUnivaluePath = function(root) {
    let best = 0;
    const dfs = (node) => {
        if (node === null) return 0;
        const left = dfs(node.left);
        const right = dfs(node.right);
        const leftPath = node.left !== null && node.left.val === node.val ? left + 1 : 0;
        const rightPath = node.right !== null && node.right.val === node.val ? right + 1 : 0;
        best = Math.max(best, leftPath + rightPath);
        return Math.max(leftPath, rightPath);
    };
    dfs(root);
    return best;
};
