// LeetCode 2608 - Shortest Cycle in a Graph
// https://leetcode.com/problems/shortest-cycle-in-a-graph/

/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var findShortestCycle = function(n, edges) {
    const g = Array.from({ length: n }, () => []);
    for (const e of edges) {
        g[e[0]].push(e[1]);
        g[e[1]].push(e[0]);
    }
    const INF = 1000000000;
    let ans = INF;
    for (let start = 0; start < n; ++start) {
        const dist = new Array(n).fill(-1);
        const parent = new Array(n).fill(-1);
        const q = [start];
        dist[start] = 0;
        while (q.length) {
            const u = q.shift();
            for (const v of g[u]) {
                if (dist[v] < 0) {
                    dist[v] = dist[u] + 1;
                    parent[v] = u;
                    q.push(v);
                } else if (parent[u] !== v) {
                    const c = dist[u] + dist[v] + 1;
                    if (c < ans) ans = c;
                }
            }
        }
    }
    return ans === INF ? -1 : ans;
};
