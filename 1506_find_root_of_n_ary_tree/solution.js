// LeetCode 1506 - Find Root of N-Ary Tree
// https://leetcode.com/problems/find-root-of-n-ary-tree/

/**
 * @param {Node[]} tree
 * @return {Node}
 */
var findRoot = function(tree) {
    let value = 0;
    const nodes = new Map();
    for (const node of tree) {
        nodes.set(node.val, node);
        value ^= node.val;
        for (const child of node.children || []) value ^= child.val;
    }
    return nodes.get(value);
};
