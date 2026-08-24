// LeetCode 2203 - Minimum Weighted Subgraph With the Required Paths
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

export class MinHeap {
    constructor(cmp: any) {
    this.a = [];
    this.cmp = cmp || ((x, y) => x - y);
}
    _up(i: any): any {
    const a = this.a, cmp = this.cmp;
    while (i > 0) {
        const p = (i - 1) >> 1;
        if (cmp(a[i], a[p]) >= 0) break;
        [a[i], a[p]] = [a[p], a[i]];
        i = p;
    }
}
    _down(i: any): any {
    const a = this.a, cmp = this.cmp, n = a.length;
    while (true) {
        let s = i, l = i * 2 + 1, r = l + 1;
        if (l < n && cmp(a[l], a[s]) < 0) s = l;
        if (r < n && cmp(a[r], a[s]) < 0) s = r;
        if (s === i) break;
        [a[i], a[s]] = [a[s], a[i]];
        i = s;
    }
}
    push(x: any): any { this.a.push(x); this._up(this.a.length - 1); }
    pop(): any {
    const a = this.a;
    if (!a.length) return undefined;
    const top = a[0], last = a.pop();
    if (a.length) { a[0] = last; this._down(0); }
    return top;
}
    peek(): any { return this.a[0]; }
    size(): any { return this.a.length; }
}

export function minimumWeight(n: number, edges: number[][], src1: number, src2: number, dest: number): number {
    const INF = Number.MAX_SAFE_INTEGER;
    function dijkstra(g: any, src: any): any {
        const dist = new Array(n).fill(INF);
        dist[src] = 0;
        const pq = new MinHeap((a, b) => a[0] - b[0]);
        pq.push([0, src]);
        while (pq.size()) {
            const [d, u] = pq.pop();
            if (d !== dist[u]) continue;
            for (const [v, w] of g[u]) {
                if (d + w < dist[v]) {
                    dist[v] = d + w;
                    pq.push([dist[v], v]);
                }
            }
        }
        return dist;
    }    const g = Array.from({length: n}, () => []);
    const rg = Array.from({length: n}, () => []);
    for (const e of edges) {
        g[e[0]].push([e[1], e[2]]);
        rg[e[1]].push([e[0], e[2]]);
    }
    const d1 = dijkstra(g, src1);
    const d2 = dijkstra(g, src2);
    const dd = dijkstra(rg, dest);
    let ans = INF;
    for (let i = 0; i < n; i++) {
        if (d1[i] >= INF || d2[i] >= INF || dd[i] >= INF) continue;
        ans = Math.min(ans, d1[i] + d2[i] + dd[i]);
    }
    return ans >= INF ? -1 : ans;
}
