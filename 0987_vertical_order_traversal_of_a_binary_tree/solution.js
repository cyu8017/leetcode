// LeetCode 0987 - Vertical Order Traversal of a Binary Tree
// https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

/**
 * @param {TreeNode} root
 * @return {number[][]}
 */
var verticalTraversal = function(root) {
    const nodes = [];
    const dfs = (node, row, col) => {
        if (!node) return;
        nodes.push([col, row, node.val]);
        dfs(node.left, row + 1, col - 1);
        dfs(node.right, row + 1, col + 1);
    };
    dfs(root, 0, 0);
    nodes.sort((a, b) => a[0] !== b[0] ? a[0] - b[0] : (a[1] !== b[1] ? a[1] - b[1] : a[2] - b[2]));
    const byCol = new Map();
    for (const t of nodes) {
        if (!byCol.has(t[0])) byCol.set(t[0], []);
        byCol.get(t[0]).push(t[2]);
    }
    return [...byCol.keys()].sort((a,b)=>a-b).map(k => byCol.get(k));
};
