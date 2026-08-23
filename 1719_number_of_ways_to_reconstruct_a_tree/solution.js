// LeetCode 1719 - Number Of Ways To Reconstruct A Tree
// https://leetcode.com/problems/number-of-ways-to-reconstruct-a-tree/

/**
 * @param {number[][]} pairs
 * @return {number}
 */
var checkWays = function(pairs) {
    const graph = new Map();
    for (const [a, b] of pairs) {
        if (!graph.has(a)) {
            graph.set(a, new Set());
        }
        if (!graph.has(b)) {
            graph.set(b, new Set());
        }
        graph.get(a).add(b);
        graph.get(b).add(a);
    }
    const nodes = [...graph.keys()];
    const n = nodes.length;
    let root = null;
    for (const node of nodes) {
        if (graph.get(node).size === n - 1) {
            root = node;
            break;
        }
    }
    if (root === null) {
        return 0;
    }
    let ans = 1;
    for (const node of nodes) {
        if (node === root) {
            continue;
        }
        let parent = null;
        let parentDegree = n + 1;
        for (const nei of graph.get(node)) {
            if (graph.get(nei).size >= graph.get(node).size && graph.get(nei).size < parentDegree) {
                parent = nei;
                parentDegree = graph.get(nei).size;
            }
        }
        if (parent === null) {
            return 0;
        }
        for (const nei of graph.get(node)) {
            if (nei !== parent && !graph.get(parent).has(nei)) {
                return 0;
            }
        }
        if (graph.get(parent).size === graph.get(node).size) {
            ans = 2;
        }
    }
    return ans;
};
