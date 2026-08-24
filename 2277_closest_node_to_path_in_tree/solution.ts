// LeetCode 2277 - Closest Node to Path in Tree
// https://leetcode.com/problems/closest-node-to-path-in-tree/

class Node {
    val: number;
    children: Node[];
    constructor(val?: number, children?: Node[]) {
        this.val = val ?? 0;
        this.children = children ?? [];
    }
}

export function closestNode(n: any, edges: any, query: any): any {
    const LOG = 17;
    const g = Array.from({length: n}, () => []);
    for (const e of edges) {
        g[e[0]].push(e[1]);
        g[e[1]].push(e[0]);
    }
    const up = Array.from({length: LOG}, () => new Array(n).fill(0));
    const depth = new Array(n).fill(0);
    const dfs = (u, p) => {
        up[0][u] = p;
        for (const v of g[u]) if (v !== p) {
            depth[v] = depth[u] + 1;
            dfs(v, u);
        }
    };
    dfs(0, 0);
    for (let k = 1; k < LOG; k++)
        for (let v = 0; v < n; v++)
            up[k][v] = up[k - 1][up[k - 1][v]];
    const lift = (v, d) => {
        for (let k = 0; k < LOG; k++)
            if (((d >> k) & 1) !== 0) v = up[k][v];
        return v;
    };
    const lca = (a, b) => {
        if (depth[a] < depth[b]) [a, b] = [b, a];
        a = lift(a, depth[a] - depth[b]);
        if (a === b) return a;
        for (let k = LOG - 1; k >= 0; k--) {
            if (up[k][a] !== up[k][b]) {
                a = up[k][a];
                b = up[k][b];
            }
        }
        return up[0][a];
    };
    const dist = (a, b) => {
        const c = lca(a, b);
        return depth[a] + depth[b] - 2 * depth[c];
    };
    const ans = new Array(query.length);
    for (let i = 0; i < query.length; i++) {
        const a = query[i][0], b = query[i][1], x = query[i][2];
        const cands = [lca(a, b), lca(a, x), lca(b, x)];
        let best = cands[0], bestD = dist(cands[0], x);
        for (let t = 1; t < 3; t++) {
            const d = dist(cands[t], x);
            if (d < bestD) { bestD = d; best = cands[t]; }
        }
        ans[i] = best;
    }
    return ans;
}
