// LeetCode 3608 - Minimum Time for K Connected Components
// https://leetcode.com/problems/minimum-time-for-k-connected-components/

export class UnionFind3608 {
    constructor(n: any) {
    this.p = new Array(n);
    this.size = new Array(n);
    for (let i = 0; i < n; i++) { this.p[i] = i; this.size[i] = 1; }
}
    find(x: any): any {
    if (this.p[x] !== x) this.p[x] = this.find(this.p[x]);
    return this.p[x];
}
    unite(a: any, b: any): any {
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
}
}

export function minTime(n: any, edges: any, k: any): any {
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
}
