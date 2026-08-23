// LeetCode 1579 - Remove Max Number of Edges to Keep Graph Fully Traversable
// https://leetcode.com/problems/remove-max-number-of-edges-to-keep-graph-fully-traversable/

/**
 * @param {number} n
 * @param {number[][]} edges
 * @return {number}
 */
var maxNumEdgesToRemove = function(n, edges) {
    class DSU {
        constructor(n) {
            this.parent = Array.from({ length: n + 1 }, (_, i) => i);
            this.components = n;
        }
        find(x) {
            while (x !== this.parent[x]) {
                this.parent[x] = this.parent[this.parent[x]];
                x = this.parent[x];
            }
            return x;
        }
        union(a, b) {
            a = this.find(a); b = this.find(b);
            if (a === b) return false;
            this.parent[a] = b;
            this.components--;
            return true;
        }
    }
    const alice = new DSU(n), bob = new DSU(n);
    let used = 0;
    for (const [t, u, v] of edges) {
        if (t === 3) {
            const merged = alice.union(u, v);
            bob.union(u, v);
            if (merged) used++;
        }
    }
    for (const [t, u, v] of edges) {
        if (t === 1) { if (alice.union(u, v)) used++; }
        else if (t === 2) { if (bob.union(u, v)) used++; }
    }
    return alice.components === 1 && bob.components === 1 ? edges.length - used : -1;
};
