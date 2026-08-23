// LeetCode 0979 - Distribute Coins in Binary Tree
// https://leetcode.com/problems/distribute-coins-in-binary-tree/

function TreeNode(val, left, right) {
    this.val = (val === undefined ? 0 : val);
    this.left = (left === undefined ? null : left);
    this.right = (right === undefined ? null : right);
}

/**
 * @param {TreeNode} root
 * @return {number}
 */
var distributeCoins = function(root) {
    let ans = 0;
    const dfs = (node) => {
        if (!node) return 0;
        const left = dfs(node.left);
        const right = dfs(node.right);
        ans += Math.abs(left) + Math.abs(right);
        return node.val + left + right - 1;
    };
    dfs(root);
    return ans;
};
