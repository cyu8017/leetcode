// LeetCode 3123 - Find Edges in Shortest Paths
// https://leetcode.com/problems/find-edges-in-shortest-paths/

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
 * @return {boolean[]}
 */
var findAnswer = function(n, edges) {
    const g = Array.from({ length: n }, () => []);
    for (let i = 0; i < edges.length; i++) {
        const a = edges[i][0], b = edges[i][1], w = edges[i][2];
        g[a].push([b, w, i]);
        g[b].push([a, w, i]);
    }
    const INF = 1 << 30;
    const dist = new Array(n).fill(INF);
    dist[0] = 0;
    const pq = new MinHeap((a, b) => a[0] - b[0]);
    pq.push([0, 0]);
    while (pq.size()) {
        const [da, a] = pq.pop();
        if (da > dist[a]) continue;
        for (const [b, w] of g[a]) {
            if (dist[b] > dist[a] + w) {
                dist[b] = dist[a] + w;
                pq.push([dist[b], b]);
            }
        }
    }
    const ans = new Array(edges.length).fill(false);
    if (dist[n - 1] === INF) return ans;
    const q = [n - 1];
    while (q.length) {
        const a = q.shift();
        for (const [b, w, i] of g[a]) {
            if (dist[a] === dist[b] + w) {
                ans[i] = true;
                q.push(b);
            }
        }
    }
    return ans;
};
