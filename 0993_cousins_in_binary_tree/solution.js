// LeetCode 0993 - Cousins in Binary Tree
// https://leetcode.com/problems/cousins-in-binary-tree/

/**
 * @param {TreeNode} root
 * @param {number} x
 * @param {number} y
 * @return {boolean}
 */
var isCousins = function(root, x, y) {
    const depth = new Map();
    const parent = new Map();
    const dfs = (node, p, d) => {
        if (!node) return;
        depth.set(node.val, d);
        parent.set(node.val, p);
        dfs(node.left, node, d + 1);
        dfs(node.right, node, d + 1);
    };
    dfs(root, null, 0);
    return depth.get(x) === depth.get(y) && parent.get(x) !== parent.get(y);
};
