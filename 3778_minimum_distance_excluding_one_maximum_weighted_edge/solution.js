// LeetCode 3778 - Minimum Distance Excluding One Maximum Weighted Edge
// https://leetcode.com/problems/minimum_distance_excluding_one_maximum_weighted_edge/

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
var minCostExcludingMax = function(n, edges) {
    const g = Array.from({length: n}, () => []);
    for (const e of edges) {
        const u = e[0], v = e[1], w = e[2];
        g[u].push([v, w]);
        g[v].push([u, w]);
    }
    const INF = Number.MAX_SAFE_INTEGER;
    const dist = Array.from({length: n}, () => [INF, INF]);
    dist[0][0] = 0;
    const pq = new MinHeap((a, b) => a[0] - b[0]);
    pq.push([0, 0, 0]);
    while (pq.size()) {
        const cur = pq.pop();
        const c = cur[0], u = cur[1], used = cur[2];
        if (c > dist[u][used]) continue;
        if (u === n - 1 && used === 1) return c;
        for (const e of g[u]) {
            const v = e[0], w = e[1];
            let nxt = c + w;
            if (nxt < dist[v][used]) {
                dist[v][used] = nxt;
                pq.push([nxt, v, used]);
            }
            if (used === 0) {
                nxt = c;
                if (nxt < dist[v][1]) {
                    dist[v][1] = nxt;
                    pq.push([nxt, v, 1]);
                }
            }
        }
    }
    return dist[n - 1][1];
};
