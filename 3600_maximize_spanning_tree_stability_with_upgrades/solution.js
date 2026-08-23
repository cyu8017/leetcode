// LeetCode 3600 - Maximize Spanning Tree Stability with Upgrades
// https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/

function UnionFind3600(n) {
    this.p = new Array(n);
    this.size = new Array(n);
    this.cnt = n;
    for (let i = 0; i < n; i++) { this.p[i] = i; this.size[i] = 1; }
}
UnionFind3600.prototype.find = function(x) {
    if (this.p[x] !== x) this.p[x] = this.find(this.p[x]);
    return this.p[x];
};
UnionFind3600.prototype.unite = function(a, b) {
    let pa = this.find(a), pb = this.find(b);
    if (pa === pb) return false;
    if (this.size[pa] > this.size[pb]) {
        this.p[pb] = pa;
        this.size[pa] += this.size[pb];
    } else {
        this.p[pa] = pb;
        this.size[pb] += this.size[pa];
    }
    this.cnt--;
    return true;
};
var maxStability = function(n, edges, k) {
    function check(lim) {
        const uf = new UnionFind3600(n);
        for (const e of edges) if (e[2] >= lim) uf.unite(e[0], e[1]);
        let rem = k;
        for (const e of edges) {
            if (e[2] * 2 >= lim && rem > 0) {
                if (uf.unite(e[0], e[1])) rem--;
            }
        }
        return uf.cnt === 1;
    }
    const uf = new UnionFind3600(n);
    let mn = 1000000;
    for (const e of edges) {
        if (e[3] === 1) {
            mn = Math.min(mn, e[2]);
            if (!uf.unite(e[0], e[1])) return -1;
        }
    }
    for (const e of edges) uf.unite(e[0], e[1]);
    if (uf.cnt > 1) return -1;
    let l = 1, r = mn;
    while (l < r) {
        const mid = (l + r + 1) >> 1;
        if (check(mid)) l = mid;
        else r = mid - 1;
    }
    return l;
};
