// LeetCode 1810 - Minimum Path Cost in a Hidden Grid
// https://leetcode.com/problems/minimum-path-cost-in-a-hidden-grid/

/**
 * @param {number[][]} grid
 * @param {number} r1
 * @param {number} c1
 * @param {number} r2
 * @param {number} c2
 * @return {number}
 */
var findShortestPath = function(grid, r1, c1, r2, c2) {
    if (r1 === r2 && c1 === c2) return 0;
    const m = grid.length, n = grid[0].length;
    const dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]];
    const INF = Number.POSITIVE_INFINITY;
    const dist = Array.from({ length: m }, () => Array(n).fill(INF));
    const heap = [];

    const push = (item) => {
        heap.push(item);
        let i = heap.length - 1;
        while (i > 0) {
            const p = (i - 1) >> 1;
            if (heap[p][0] <= heap[i][0]) break;
            [heap[p], heap[i]] = [heap[i], heap[p]];
            i = p;
        }
    };
    const pop = () => {
        const top = heap[0];
        const last = heap.pop();
        if (heap.length === 0) return top;
        heap[0] = last;
        let i = 0;
        const len = heap.length;
        while (true) {
            let s = i;
            const l = 2 * i + 1, r = 2 * i + 2;
            if (l < len && heap[l][0] < heap[s][0]) s = l;
            if (r < len && heap[r][0] < heap[s][0]) s = r;
            if (s === i) break;
            [heap[s], heap[i]] = [heap[i], heap[s]];
            i = s;
        }
        return top;
    };

    dist[r1][c1] = 0;
    push([0, r1, c1]);
    while (heap.length) {
        const [d, r, c] = pop();
        if (r === r2 && c === c2) return d;
        if (d > dist[r][c]) continue;
        for (const [dr, dc] of dirs) {
            const nr = r + dr, nc = c + dc;
            if (nr < 0 || nr >= m || nc < 0 || nc >= n || grid[nr][nc] === 0) continue;
            const nd = d + grid[nr][nc];
            if (nd < dist[nr][nc]) {
                dist[nr][nc] = nd;
                push([nd, nr, nc]);
            }
        }
    }
    return -1;
};
