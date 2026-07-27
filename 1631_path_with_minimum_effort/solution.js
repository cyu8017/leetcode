// LeetCode 1631 - Path With Minimum Effort
// https://leetcode.com/problems/path-with-minimum-effort/

/**
 * @param {number[][]} heights
 * @return {number}
 */
var minimumEffortPath = function(heights) {
    const m = heights.length, n = heights[0].length;
    const dist = Array.from({ length: m }, () => Array(n).fill(Infinity));
    dist[0][0] = 0;
    const heap = [[0, 0, 0]];
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
        if (!heap.length) return top;
        heap[0] = last;
        let i = 0;
        while (true) {
            let s = i;
            const l = 2 * i + 1, r = 2 * i + 2;
            if (l < heap.length && heap[l][0] < heap[s][0]) s = l;
            if (r < heap.length && heap[r][0] < heap[s][0]) s = r;
            if (s === i) break;
            [heap[s], heap[i]] = [heap[i], heap[s]];
            i = s;
        }
        return top;
    };
    while (heap.length) {
        const [effort, i, j] = pop();
        if (i === m - 1 && j === n - 1) return effort;
        if (effort !== dist[i][j]) continue;
        for (const [di, dj] of [[1, 0], [-1, 0], [0, 1], [0, -1]]) {
            const x = i + di, y = j + dj;
            if (x >= 0 && x < m && y >= 0 && y < n) {
                const nd = Math.max(effort, Math.abs(heights[i][j] - heights[x][y]));
                if (nd < dist[x][y]) {
                    dist[x][y] = nd;
                    push([nd, x, y]);
                }
            }
        }
    }
    return 0;
};
