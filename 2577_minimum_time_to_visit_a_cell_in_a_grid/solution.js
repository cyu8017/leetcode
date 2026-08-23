// LeetCode 2577 - Minimum Time to Visit a Cell In a Grid
// https://leetcode.com/problems/minimum-time-to-visit-a-cell-in-a-grid/

function Heap(cmp) {
    this.a = [];
    this.cmp = cmp;
}
Heap.prototype._up = function(i) {
    const a = this.a, cmp = this.cmp;
    while (i > 0) {
        const p = (i - 1) >> 1;
        if (cmp(a[i], a[p]) >= 0) break;
        [a[i], a[p]] = [a[p], a[i]];
        i = p;
    }
};
Heap.prototype._down = function(i) {
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
Heap.prototype.push = function(x) { this.a.push(x); this._up(this.a.length - 1); };
Heap.prototype.pop = function() {
    const a = this.a;
    if (!a.length) return undefined;
    const top = a[0], last = a.pop();
    if (a.length) { a[0] = last; this._down(0); }
    return top;
};
Heap.prototype.size = function() { return this.a.length; };

/**
 * @param {number[][]} grid
 * @return {number}
 */
var minimumTime = function(grid) {
    if (grid[0][1] > 1 && grid[1][0] > 1) return -1;
    const m = grid.length, n = grid[0].length;
    const dist = Array.from({ length: m }, () => new Array(n).fill(1 << 30));
    const h = new Heap((a, b) => a[0] - b[0]);
    h.push([0, 0, 0]);
    dist[0][0] = 0;
    const dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]];
    while (h.size()) {
        const cur = h.pop();
        const t = cur[0], r = cur[1], c = cur[2];
        if (r === m - 1 && c === n - 1) return t;
        if (t > dist[r][c]) continue;
        for (const d of dirs) {
            const nr = r + d[0], nc = c + d[1];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            let nt = t + 1;
            if (nt < grid[nr][nc]) {
                let wait = grid[nr][nc] - nt;
                if (wait % 2 === 1) wait++;
                nt += wait;
            }
            if (nt < dist[nr][nc]) {
                dist[nr][nc] = nt;
                h.push([nt, nr, nc]);
            }
        }
    }
    return -1;
};
