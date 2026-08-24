// LeetCode 2737 - Find the Closest Marked Node
// https://leetcode.com/problems/find-the-closest-marked-node/

class Node {
    val: number;
    children: Node[];
    constructor(val?: number, children?: Node[]) {
        this.val = val ?? 0;
        this.children = children ?? [];
    }
}

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

export function minimumDistance(n: number, edges: number[][], s: number, marked: number[]): number {
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
}
