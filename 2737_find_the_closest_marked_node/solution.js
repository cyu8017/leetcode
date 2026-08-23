// LeetCode 2737 - Find the Closest Marked Node
// https://leetcode.com/problems/find-the-closest-marked-node/

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
 * @param {number} s
 * @param {number[]} marked
 * @return {number}
 */
var minimumDistance = function(n, edges, s, marked) {
    const g = Array.from({length: n}, () => []);
    for (const [u, v, w] of edges) g[u].push([v, w]);
    const mark = new Set(marked);
    const dist = Array(n).fill(Math.floor(Number.MAX_SAFE_INTEGER / 4));
    dist[s] = 0;
    const pq = new MinHeap((a, b) => a[0] - b[0]);
    pq.push([0, s]);
    while (pq.size()) {
        const [d, u] = pq.pop();
        if (mark.has(u)) return d;
        if (d > dist[u]) continue;
        for (const [v, w] of g[u]) {
            if (d + w < dist[v]) {
                dist[v] = d + w;
                pq.push([dist[v], v]);
            }
        }
    }
    return -1;
};
