// LeetCode 2503 - Maximum Number of Points From Grid Queries
// https://leetcode.com/problems/maximum-number-of-points-from-grid-queries/

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

export function maxPoints(grid: number[][], queries: number[]): number[] {
    const m = grid.length, n = grid[0].length;
    const order = Array.from({ length: queries.length }, (_, i) => i);
    order.sort((a, b) => queries[a] - queries[b]);
    const ans = Array(queries.length);
    const visited = Array.from({ length: m }, () => Array(n).fill(false));
    const pq = new MinHeap((a, b) => a[0] - b[0]);
    pq.push([grid[0][0], 0, 0]);
    visited[0][0] = true;
    let points = 0;
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    for (const qi of order) {
        const q = queries[qi];
        while (pq.size() && pq.peek()[0] < q) {
            const [, r, c] = pq.pop();
            points++;
            for (const [dr, dc] of dirs) {
                const nr = r + dr, nc = c + dc;
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && !visited[nr][nc]) {
                    visited[nr][nc] = true;
                    pq.push([grid[nr][nc], nr, nc]);
                }
            }
        }
        ans[qi] = points;
    }
    return ans;
}
