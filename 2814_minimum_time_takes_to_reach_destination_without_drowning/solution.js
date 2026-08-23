// LeetCode 2814 - Minimum Time Takes to Reach Destination Without Drowning
// https://leetcode.com/problems/minimum-time-takes-to-reach-destination-without-drowning/

/**
 * @param {string[][]} land
 * @return {number}
 */
var minimumSeconds = function(land) {
    const m = land.length, n = land[0].length;
    const INF = 1e9;
    const water = Array.from({length: m}, () => Array(n).fill(INF));
    const wq = [];
    let sx = 0, sy = 0, dx = 0, dy = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            const cell = land[i][j];
            if (cell === '*') {
                water[i][j] = 0;
                wq.push([i, j]);
            } else if (cell === 'S') { sx = i; sy = j; }
            else if (cell === 'D') { dx = i; dy = j; }
        }
    }
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    for (let h = 0; h < wq.length; h++) {
        const [x, y] = wq[h];
        for (const [ddx, ddy] of dirs) {
            const ni = x + ddx, nj = y + ddy;
            if (ni < 0 || nj < 0 || ni >= m || nj >= n) continue;
            const cell = land[ni][nj];
            if (cell === 'X' || cell === 'D') continue;
            if (water[ni][nj] > water[x][y] + 1) {
                water[ni][nj] = water[x][y] + 1;
                wq.push([ni, nj]);
            }
        }
    }
    const dist = Array.from({length: m}, () => Array(n).fill(-1));
    const q = [[sx, sy]];
    dist[sx][sy] = 0;
    for (let h = 0; h < q.length; h++) {
        const [x, y] = q[h];
        if (x === dx && y === dy) return dist[x][y];
        for (const [ddx, ddy] of dirs) {
            const ni = x + ddx, nj = y + ddy;
            if (ni < 0 || nj < 0 || ni >= m || nj >= n || dist[ni][nj] !== -1) continue;
            if (land[ni][nj] === 'X') continue;
            const nd = dist[x][y] + 1;
            if (land[ni][nj] !== 'D' && nd >= water[ni][nj]) continue;
            dist[ni][nj] = nd;
            q.push([ni, nj]);
        }
    }
    return -1;
};
