// LeetCode 3108 - Minimum Cost Walk in Weighted Graph
// https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

export function minimumCost(n: number, edges: number[][], query: number[][]): number[] {
    const p = new Array(n), size = new Array(n).fill(1);
    for (let i = 0; i < n; i++) p[i] = i;
    const find = (x) => {
        if (p[x] !== x) p[x] = find(p[x]);
        return p[x];
    };
    const unite = (a, b) => {
        let pa = find(a), pb = find(b);
        if (pa === pb) return;
        if (size[pa] > size[pb]) {
            p[pb] = pa;
            size[pa] += size[pb];
        } else {
            p[pa] = pb;
            size[pb] += size[pa];
        }
    };
    const g = new Array(n).fill(-1);
    for (const e of edges) unite(e[0], e[1]);
    for (const e of edges) {
        const root = find(e[0]);
        g[root] &= e[2];
    }
    const ans = new Array(query.length);
    for (let i = 0; i < query.length; i++) {
        const u = query[i][0], v = query[i][1];
        if (u === v) ans[i] = 0;
        else {
            const a = find(u), b = find(v);
            ans[i] = a === b ? g[a] : -1;
        }
    }
    return ans;
}
