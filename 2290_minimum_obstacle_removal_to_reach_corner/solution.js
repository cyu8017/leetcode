// LeetCode 2290 - Minimum Obstacle Removal to Reach Corner
// https://leetcode.com/problems/minimum-obstacle-removal-to-reach-corner/

var minimumObstacles = function(grid) {
    const m = grid.length, n = grid[0].length;
    const dist = Array.from({length: m}, () => new Array(n).fill(Infinity));
    dist[0][0] = 0;
    const dq = [[0, 0]];
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    while (dq.length) {
        const [r, c] = dq.shift();
        for (const d of dirs) {
            const nr = r + d[0], nc = c + d[1];
            if (nr < 0 || nr >= m || nc < 0 || nc >= n) continue;
            const nd = dist[r][c] + grid[nr][nc];
            if (nd < dist[nr][nc]) {
                dist[nr][nc] = nd;
                if (grid[nr][nc] === 0) dq.unshift([nr, nc]);
                else dq.push([nr, nc]);
            }
        }
    }
    return dist[m - 1][n - 1];
};
