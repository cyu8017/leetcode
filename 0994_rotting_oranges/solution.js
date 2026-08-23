// LeetCode 0994 - Rotting Oranges
// https://leetcode.com/problems/rotting-oranges/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var orangesRotting = function(grid) {
    const m = grid.length, n = grid[0].length;
    const q = [];
    let fresh = 0;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            if (grid[i][j] === 2) q.push([i, j]);
            else if (grid[i][j] === 1) fresh++;
        }
    }
    let minutes = 0;
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    while (q.length && fresh > 0) {
        const sz = q.length;
        for (let s = 0; s < sz; s++) {
            const [cr, cc] = q.shift();
            for (const [dr, dc] of dirs) {
                const nr = cr + dr, nc = cc + dc;
                if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] === 1) {
                    grid[nr][nc] = 2;
                    fresh--;
                    q.push([nr, nc]);
                }
            }
        }
        minutes++;
    }
    return fresh === 0 ? minutes : -1;
};
