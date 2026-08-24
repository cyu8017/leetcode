// LeetCode 3553 - Minimum Weighted Subgraph With the Required Paths II
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/

export function minimumWeight(edges: any, queries: any): any {
    const LOG = 17;
    const n = edges.length + 1;
    const g = Array.from({length: n}, () => []);
    for (const e of edges) {
        g[e[0]].push([e[1], e[2]]);
        g[e[1]].push([e[0], e[2]]);
    }
    const parent = Array.from({length: LOG}, () => new Array(n).fill(-1));
    const depth = new Array(n).fill(0);
    const dist = new Array(n).fill(0);
    function dfs(u: any, p: any): any {
        parent[0][u] = p;
        for (const e of g[u]) {
            const to = e[0], w = e[1];
            if (to === p) continue;
            depth[to] = depth[u] + 1;
            dist[to] = dist[u] + w;
            dfs(to, u);
        }
    }    function lca(u: any, v: any): any {
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
    }    function path(u: any, v: any): any {
        const a = lca(u, v);
        return dist[u] + dist[v] - 2 * dist[a];
    }    dfs(0, -1);
    for (let k = 1; k < LOG; k++)
        for (let v = 0; v < n; v++)
            if (parent[k - 1][v] !== -1) parent[k][v] = parent[k - 1][parent[k - 1][v]];
    const ans = new Array(queries.length);
    for (let i = 0; i < queries.length; i++) {
        const a = queries[i][0], b = queries[i][1], c = queries[i][2];
        ans[i] = Math.floor((path(a, b) + path(b, c) + path(a, c)) / 2);
    }
    return ans;
}
