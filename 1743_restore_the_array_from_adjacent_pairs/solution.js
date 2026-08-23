// LeetCode 1743 - Restore the Array From Adjacent Pairs
// https://leetcode.com/problems/restore-the-array-from-adjacent-pairs/

/**
 * @param {number[][]} adjacentPairs
 * @return {number[]}
 */
var restoreArray = function(adjacentPairs) {
    const graph = new Map();
    for (const [a, b] of adjacentPairs) {
        if (!graph.has(a)) {
            graph.set(a, []);
        }
        if (!graph.has(b)) {
            graph.set(b, []);
        }
        graph.get(a).push(b);
        graph.get(b).push(a);
    }
    let start = 0;
    for (const [node, neighbors] of graph) {
        if (neighbors.length === 1) {
            start = node;
            break;
        }
    }
    const ans = [start];
    let prev = null;
    while (ans.length < graph.size) {
        const cur = ans[ans.length - 1];
        const neighbors = graph.get(cur);
        const nxt = neighbors[0] !== prev ? neighbors[0] : neighbors[1];
        ans.push(nxt);
        prev = cur;
    }
    return ans;
};
