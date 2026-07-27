// LeetCode 1676 - Lowest Common Ancestor of a Binary Tree IV
// https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/

/**
 * @param {object} root
 * @param {object[]|number[]} nodes
 * @return {object}
 */
var lowestCommonAncestor = function(root, nodes) {
    const targets = new Set(nodes);
    const match = (node) => {
        if (!node) return false;
        if (targets.has(node)) return true;
        return targets.has(node.val);
    };
    const dfs = (node) => {
        if (!node) return null;
        const l = dfs(node.left);
        const r = dfs(node.right);
        if (match(node) || (l && r)) return node;
        return l || r;
    };
    return dfs(root);
};
