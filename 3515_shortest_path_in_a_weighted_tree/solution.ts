// LeetCode 3515 - Shortest Path in a Weighted Tree
// https://leetcode.com/problems/shortest-path-in-a-weighted-tree/

export function treeQueries(n: any, edges: any, queries: any): any {
    const g = Array.from({length: n + 1}, () => []);
    const weight = new Map();
    for (const e of edges) {
        const u = e[0], v = e[1], w = e[2];
        g[u].push([v, w]);
        g[v].push([u, w]);
        const a = Math.min(u, v), b = Math.max(u, v);
        weight.set((BigInt(a) << 32n) | BigInt(b), w);
    }
    const inT = new Array(n + 1).fill(0);
    const outT = new Array(n + 1).fill(0);
    const dist = new Array(n + 1).fill(0);
    const parent = new Array(n + 1).fill(0);
    let time = 0;
    function dfs(u: any, p: any): any {
        inT[u] = time++;
        for (const e of g[u]) {
            const to = e[0], w = e[1];
            if (to === p) continue;
            parent[to] = u;
            dist[to] = dist[u] + w;
            dfs(to, u);
        }
        outT[u] = time - 1;
    }    dfs(1, 0);
    const bit = new Array(n + 2).fill(0);
    function add(i: any, v: any): any {
        for (; i <= n; i += i & -i) bit[i] += v;
    }    function rangeAdd(l: any, r: any, v: any): any {
        add(l + 1, v);
        add(r + 2, -v);
    }    function point(i: any): any {
        let s = 0;
        for (i++; i > 0; i -= i & -i) s += bit[i];
        return s;
    }    for (let i = 1; i <= n; i++) rangeAdd(inT[i], inT[i], dist[i]);
    const ans = [];
    for (const q of queries) {
        if (q[0] === 1) {
            const u = q[1], v = q[2], nw = q[3];
            const a = Math.min(u, v), b = Math.max(u, v);
            const key = (BigInt(a) << 32n) | BigInt(b);
            const ow = weight.get(key);
            const delta = nw - ow;
            weight.set(key, nw);
            const child = parent[u] === v ? u : v;
            rangeAdd(inT[child], outT[child], delta);
        } else {
            ans.push(point(inT[q[1]]));
        }
    }
    return ans;
}
