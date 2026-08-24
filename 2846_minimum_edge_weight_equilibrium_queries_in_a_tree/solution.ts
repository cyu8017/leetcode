// LeetCode 2846 - Minimum Edge Weight Equilibrium Queries in a Tree
// https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/

export function minOperationsQueries(n: number, edges: number[][], queries: number[][]): number[] {
    const LOG = 15;
    const g = Array.from({ length: n }, () => []);
    for (const [a, b, w] of edges) {
        g[a].push([b, w]);
        g[b].push([a, w]);
    }
    const up = Array.from({ length: LOG }, () => Array(n).fill(0));
    const depth = Array(n).fill(0);
    const cnt = Array.from({ length: n }, () => Array(27).fill(0));
    const dfs = (u, p) => {
        up[0][u] = p;
        for (const [v, w] of g[u]) {
            if (v === p) continue;
            depth[v] = depth[u] + 1;
            for (let i = 0; i < 27; i++) cnt[v][i] = cnt[u][i];
            cnt[v][w]++;
            dfs(v, u);
        }
    };
    dfs(0, 0);
    for (let j = 1; j < LOG; j++)
        for (let i = 0; i < n; i++) up[j][i] = up[j - 1][up[j - 1][i]];
    const lca = (a, b) => {
        if (depth[a] < depth[b]) [a, b] = [b, a];
        let diff = depth[a] - depth[b];
        for (let j = 0; j < LOG; j++) if ((diff & (1 << j)) !== 0) a = up[j][a];
        if (a === b) return a;
        for (let j = LOG - 1; j >= 0; j--) {
            if (up[j][a] !== up[j][b]) {
                a = up[j][a];
                b = up[j][b];
            }
        }
        return up[0][a];
    };
    return queries.map(([a, b]) => {
        const c = lca(a, b);
        const total = depth[a] + depth[b] - 2 * depth[c];
        let best = 0;
        for (let w = 1; w <= 26; w++) {
            const f = cnt[a][w] + cnt[b][w] - 2 * cnt[c][w];
            if (f > best) best = f;
        }
        return total - best;
    });
}
