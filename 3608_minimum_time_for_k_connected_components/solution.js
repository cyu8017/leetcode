// LeetCode 3608 - Minimum Time for K Connected Components
// https://leetcode.com/problems/minimum-time-for-k-connected-components/

function UnionFind3608(n) {
    this.p = new Array(n);
    this.size = new Array(n);
    for (let i = 0; i < n; i++) { this.p[i] = i; this.size[i] = 1; }
}
UnionFind3608.prototype.find = function(x) {
    if (this.p[x] !== x) this.p[x] = this.find(this.p[x]);
    return this.p[x];
};
UnionFind3608.prototype.unite = function(a, b) {
    let pa = this.find(a), pb = this.find(b);
    if (pa === pb) return false;
    if (this.size[pa] > this.size[pb]) {
        this.p[pb] = pa;
        this.size[pa] += this.size[pb];
    } else {
        this.p[pa] = pb;
        this.size[pb] += this.size[pa];
    }
    return true;
};
var minTime = function(n, edges, k) {
    edges = edges.slice().sort((a, b) => a[2] - b[2]);
    const uf = new UnionFind3608(n);
    let cnt = n;
    for (let i = edges.length - 1; i >= 0; i--) {
        if (uf.unite(edges[i][0], edges[i][1])) {
            cnt--;
            if (cnt < k) return edges[i][2];
        }
    }
    return 0;
};
