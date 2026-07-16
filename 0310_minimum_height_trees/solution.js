// LeetCode 0310 - Minimum Height Trees
// https://leetcode.com/problems/minimum-height-trees/

/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number[]}
 */
var findMinHeightTrees = function(n, edges) {
    if (n <= 2) {
        return Array.from({ length: n }, (_, index) => index);
    }
    const graph = Array.from({ length: n }, () => []);
    const degree = Array(n).fill(0);
    for (const [left, right] of edges) {
        graph[left].push(right);
        graph[right].push(left);
        degree[left] += 1;
        degree[right] += 1;
    }
    let leaves = [];
    for (let node = 0; node < n; node += 1) {
        if (degree[node] === 1) {
            leaves.push(node);
        }
    }
    let remaining = n;
    while (remaining > 2) {
        remaining -= leaves.length;
        const newLeaves = [];
        for (const leaf of leaves) {
            for (const neighbor of graph[leaf]) {
                degree[neighbor] -= 1;
                if (degree[neighbor] === 1) {
                    newLeaves.push(neighbor);
                }
            }
        }
        leaves = newLeaves;
    }
    return leaves;
};
