// LeetCode 2473 - Minimum Cost to Buy Apples
// https://leetcode.com/problems/minimum-cost-to-buy-apples/

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

export function minCost(n: number, roads: number[][], appleCost: number[], k: number): number[] {
    const g = Array.from({ length: n + 1 }, () => []);
    for (const r of roads) {
        g[r[0]].push([r[1], r[2]]);
        g[r[1]].push([r[0], r[2]]);
    }
    const ans = Array(n);
    const INF = Number.MAX_SAFE_INTEGER / 4;
    for (let start = 1; start <= n; start++) {
        const dist = Array(n + 1).fill(INF);
        dist[start] = 0;
        const pq = new MinHeap((a, b) => a[0] - b[0]);
        pq.push([0, start]);
        while (pq.size()) {
            const [d, u] = pq.pop();
            if (d !== dist[u]) continue;
            for (const [v, w] of g[u]) {
                const nd = d + w;
                if (nd < dist[v]) {
                    dist[v] = nd;
                    pq.push([nd, v]);
                }
            }
        }
        let best = INF;
        for (let city = 1; city <= n; city++) {
            const cost = dist[city] * (k + 1) + appleCost[city - 1];
            if (cost < best) best = cost;
        }
        ans[start - 1] = best;
    }
    return ans;
}
