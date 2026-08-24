// LeetCode 3613 - Minimize Maximum Component Cost
// https://leetcode.com/problems/minimize-maximum-component-cost/

export function minCost(n: any, edges: any, k: any): any {
    const p = Array.from({length: n}, (_, i) => i);
    const find = (x) => (p[x] === x ? x : (p[x] = find(p[x])));
    if (k === n) return 0;
    edges.sort((a, b) => a[2] - b[2]);
    let cnt = n;
    for (const e of edges) {
        const pu = find(e[0]), pv = find(e[1]);
        if (pu !== pv) {
            p[pu] = pv;
            if (--cnt <= k) return e[2];
        }
    }
    return 0;
}
