// LeetCode 3552 - Grid Teleportation Traversal
// https://leetcode.com/problems/grid-teleportation-traversal/

var minMoves = function(matrix) {
    const m = matrix.length, n = matrix[0].length;
    const g = new Map();
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++)
            if (/[A-Za-z]/.test(matrix[i][j])) {
                if (!g.has(matrix[i][j])) g.set(matrix[i][j], []);
                g.get(matrix[i][j]).push([i, j]);
            }
    const dirs = [-1, 0, 1, 0, -1];
    const INF = 1 << 30;
    const dist = Array.from({length: m}, () => new Array(n).fill(INF));
    dist[0][0] = 0;
    const q = [[0, 0]];
    while (q.length) {
        const cur = q.shift();
        const i = cur[0], j = cur[1], d = dist[i][j];
        if (i === m - 1 && j === n - 1) return d;
        const c = matrix[i][j];
        if (g.has(c)) {
            for (const p of g.get(c)) {
                const x = p[0], y = p[1];
                if (d < dist[x][y]) {
                    dist[x][y] = d;
                    q.unshift([x, y]);
                }
            }
            g.delete(c);
        }
        for (let idx = 0; idx < 4; idx++) {
            const x = i + dirs[idx], y = j + dirs[idx + 1];
            if (0 <= x && x < m && 0 <= y && y < n && matrix[x][y] !== '#' && d + 1 < dist[x][y]) {
                dist[x][y] = d + 1;
                q.push([x, y]);
            }
        }
    }
    return -1;
};
