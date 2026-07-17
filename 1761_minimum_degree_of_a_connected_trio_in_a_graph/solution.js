// LeetCode 1761 - Minimum Degree of a Connected Trio in a Graph
// https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/

/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var minTrioDegree = function(n, edges) {
    const adj = Array.from({ length: n }, () => new Array(n).fill(false));
    const degree = new Array(n).fill(0);
    for (const [a, b] of edges) {
        adj[a - 1][b - 1] = true;
        adj[b - 1][a - 1] = true;
        degree[a - 1]++;
        degree[b - 1]++;
    }
    let best = Infinity;
    for (const [a, b] of edges) {
        const u = a - 1;
        const v = b - 1;
        for (let k = 0; k < n; k++) {
            if (adj[u][k] && adj[v][k]) {
                best = Math.min(best, degree[u] + degree[v] + degree[k] - 6);
            }
        }
    }
    return best === Infinity ? -1 : best;
};
