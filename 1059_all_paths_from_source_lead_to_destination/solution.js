// LeetCode 1059 - All Paths from Source Lead to Destination
// https://leetcode.com/problems/all-paths-from-source-lead-to-destination/

/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} source
 * @param {number} destination
 * @return {boolean}
 */
var leadsToDestination = function(n, edges, source, destination) {
    const graph = Array.from({ length: n }, () => []);
    for (const [a, b] of edges) graph[a].push(b);
    const state = new Array(n).fill(0);

    function dfs(node) {
        if (graph[node].length === 0) return node === destination;
        if (state[node] === 1) return false;
        if (state[node] === 2) return true;
        state[node] = 1;
        for (const nxt of graph[node]) {
            if (!dfs(nxt)) return false;
        }
        state[node] = 2;
        return true;
    }

    return dfs(source);
};
