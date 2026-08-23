// LeetCode 2316 - Count Unreachable Pairs of Nodes in an Undirected Graph
// https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var countPairs = function(n, edges) {
    const g = Array.from({ length: n }, () => []);
    for (const e of edges) {
        g[e[0]].push(e[1]);
        g[e[1]].push(e[0]);
    }
    const vis = Array(n).fill(false);
    const dfs = (u) => {
        vis[u] = true;
        let size = 1;
        for (const v of g[u]) if (!vis[v]) size += dfs(v);
        return size;
    };
    let ans = 0, seen = 0;
    for (let i = 0; i < n; ++i) {
        if (!vis[i]) {
            const sz = dfs(i);
            ans += sz * seen;
            seen += sz;
        }
    }
    return ans;
};
