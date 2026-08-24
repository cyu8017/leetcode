// LeetCode 3887 - Incremental Even-Weighted Cycle Queries
// https://leetcode.com/problems/incremental-even-weighted-cycle-queries/

export function countValidEdges(n: any, edges: any): any {
    const parent = new Array(n);
    const size = new Array(n);
    const parity = new Array(n).fill(0);
    for (let i = 0; i < n; i++) { parent[i] = i; size[i] = 1; }
    const find = (x) => {
        if (parent[x] === x) return [x, 0];
        const res = find(parent[x]);
        const root = res[0], p = res[1];
        parity[x] ^= p;
        parent[x] = root;
        return [root, parity[x]];
    };
    let ans = 0;
    for (const e of edges) {
        let fu = find(e[0]), fv = find(e[1]);
        let ru = fu[0], pu = fu[1], rv = fv[0], pv = fv[1];
        if (ru === rv) {
            if ((pu ^ pv) === e[2]) ans++;
            continue;
        }
        if (size[ru] < size[rv]) {
            let t = ru; ru = rv; rv = t;
            t = pu; pu = pv; pv = t;
        }
        parent[rv] = ru;
        parity[rv] = pu ^ pv ^ e[2];
        size[ru] += size[rv];
        ans++;
    }
    return ans;
}
