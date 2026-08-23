// LeetCode 3112 - Minimum Time to Visit Disappearing Nodes
// https://leetcode.com/problems/minimum-time-to-visit-disappearing-nodes/

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
 * @param {number[]} disappear
 * @return {number[]}
 */
var minimumTime = function(n, edges, disappear) {
    const g = Array.from({ length: n }, () => []);
    for (const e of edges) {
        g[e[0]].push([e[1], e[2]]);
        g[e[1]].push([e[0], e[2]]);
    }
    const INF = 1 << 30;
    const dist = new Array(n).fill(INF);
    dist[0] = 0;
    const pq = new MinHeap((a, b) => a[0] - b[0]);
    pq.push([0, 0]);
    while (pq.size()) {
        const [du, u] = pq.pop();
        if (du > dist[u]) continue;
        for (const [v, w] of g[u]) {
            if (dist[v] > dist[u] + w && dist[u] + w < disappear[v]) {
                dist[v] = dist[u] + w;
                pq.push([dist[v], v]);
            }
        }
    }
    const ans = new Array(n);
    for (let i = 0; i < n; i++)
        ans[i] = dist[i] < disappear[i] ? dist[i] : -1;
    return ans;
};
