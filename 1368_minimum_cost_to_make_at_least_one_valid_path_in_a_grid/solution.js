// LeetCode 1368 - Minimum Cost To Make At Least One Valid Path In A Grid
// https://leetcode.com/problems/minimum-cost-to-make-at-least-one-valid-path-in-a-grid/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var minCost = function(grid) {
    const m = grid.length, n = grid[0].length;
    const dist = Array.from({ length: m }, () => Array(n).fill(1e9));
    dist[0][0] = 0;
    const q = [[0, 0]];
    const dirs = [[0, 1], [0, -1], [1, 0], [-1, 0]];
    while (q.length) {
        const [r, c] = q.shift();
        for (let k = 0; k < 4; k++) {
            const [dr, dc] = dirs[k];
            const x = r + dr, y = c + dc;
            if (x >= 0 && x < m && y >= 0 && y < n) {
                const w = (k + 1) !== grid[r][c] ? 1 : 0;
                const nd = dist[r][c] + w;
                if (nd < dist[x][y]) {
                    dist[x][y] = nd;
                    if (w) q.push([x, y]);
                    else q.unshift([x, y]);
                }
            }
        }
    }
    return dist[m - 1][n - 1];
};
