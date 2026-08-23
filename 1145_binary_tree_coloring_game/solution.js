// LeetCode 1145 - Binary Tree Coloring Game
// https://leetcode.com/problems/binary-tree-coloring-game/

/**
 * @param {TreeNode} root
 * @param {number} n
 * @param {number} x
 * @return {boolean}
 */
var btreeGameWinningMove = function(root, n, x) {
    let left = 0, right = 0;
    const dfs = (node) => {
        if (!node) return 0;
        const l = dfs(node.left), r = dfs(node.right);
        if (node.val === x) {
            left = l;
            right = r;
        }
        return l + r + 1;
    };
    dfs(root);
    return Math.max(left, right, n - left - right - 1) > Math.floor(n / 2);
};
