// LeetCode 2203 - Minimum Weighted Subgraph With the Required Paths
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths/

function MinHeap(cmp) {
    this.a = [];
    this.cmp = cmp || ((x, y) => x - y);
}
MinHeap.prototype._up = function(i) {
    const a = this.a, cmp = this.cmp;
    while (i > 0) {
        const p = (i - 1) >> 1;
        if (cmp(a[i], a[p]) >= 0) break;
        [a[i], a[p]] = [a[p], a[i]];
        i = p;
    }
};
MinHeap.prototype._down = function(i) {
    const a = this.a, cmp = this.cmp, n = a.length;
    while (true) {
        let s = i, l = i * 2 + 1, r = l + 1;
        if (l < n && cmp(a[l], a[s]) < 0) s = l;
        if (r < n && cmp(a[r], a[s]) < 0) s = r;
        if (s === i) break;
        [a[i], a[s]] = [a[s], a[i]];
        i = s;
    }
};
MinHeap.prototype.push = function(x) { this.a.push(x); this._up(this.a.length - 1); };
MinHeap.prototype.pop = function() {
    const a = this.a;
    if (!a.length) return undefined;
    const top = a[0], last = a.pop();
    if (a.length) { a[0] = last; this._down(0); }
    return top;
};
MinHeap.prototype.peek = function() { return this.a[0]; };
MinHeap.prototype.size = function() { return this.a.length; };

/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} src1
 * @param {number} src2
 * @param {number} dest
 * @return {number}
 */
var minimumWeight = function(n, edges, src1, src2, dest) {
    const INF = Number.MAX_SAFE_INTEGER;
    function dijkstra(g, src) {
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
    }
    const g = Array.from({length: n}, () => []);
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
};
