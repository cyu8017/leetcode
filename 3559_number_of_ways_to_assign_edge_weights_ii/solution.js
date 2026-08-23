// LeetCode 3559 - Number of Ways to Assign Edge Weights II
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

var assignEdgeWeights = function(edges, queries) {
    const MOD = 1000000007, LOG = 17;
    const n = edges.length + 1;
    const depth = new Array(n + 1).fill(0);
    const graph = Array.from({length: n + 1}, () => []);
    const parent = Array.from({length: LOG}, () => new Array(n + 1).fill(-1));
    for (const e of edges) {
        graph[e[0]].push(e[1]);
        graph[e[1]].push(e[0]);
    }
    function dfs(u, p) {
        parent[0][u] = p;
        for (const v of graph[u]) {
            if (v !== p) {
                depth[v] = depth[u] + 1;
                dfs(v, u);
            }
        }
    }
    function lca(u, v) {
        if (depth[u] < depth[v]) { const t = u; u = v; v = t; }
        for (let k = LOG - 1; k >= 0; k--)
            if (parent[k][u] !== -1 && depth[parent[k][u]] >= depth[v]) u = parent[k][u];
        if (u === v) return u;
        for (let k = LOG - 1; k >= 0; k--)
            if (parent[k][u] !== -1 && parent[k][u] !== parent[k][v]) {
                u = parent[k][u];
                v = parent[k][v];
            }
        return parent[0][u];
    }
    function modPow(exp) {
        let base = 2n, res = 1n, m = BigInt(MOD);
        while (exp > 0) {
            if (exp & 1) res = res * base % m;
            base = base * base % m;
            exp >>= 1;
        }
        return Number(res);
    }
    dfs(1, -1);
    for (let k = 1; k < LOG; k++)
        for (let v = 1; v <= n; v++)
            if (parent[k - 1][v] !== -1) parent[k][v] = parent[k - 1][parent[k - 1][v]];
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const u = queries[i][0], v = queries[i][1];
        if (u === v) { ans[i] = 0; continue; }
        const a = lca(u, v);
        const d = depth[u] + depth[v] - 2 * depth[a];
        ans[i] = modPow(d - 1);
    }
    return ans;
};
