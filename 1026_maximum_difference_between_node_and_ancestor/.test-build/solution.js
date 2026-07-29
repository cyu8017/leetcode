"use strict";
// LeetCode 1026 - Maximum Difference Between Node and Ancestor
// https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
function maxAncestorDiff(root) {
    if (!root)
        return 0;
    const dfs = (node, lo, hi) => {
        if (!node)
            return hi - lo;
        lo = Math.min(lo, node.val);
        hi = Math.max(hi, node.val);
        return Math.max(dfs(node.left, lo, hi), dfs(node.right, lo, hi));
    };
    return dfs(root, root.val, root.val);
}
