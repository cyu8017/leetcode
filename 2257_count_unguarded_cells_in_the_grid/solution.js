// LeetCode 2257 - Count Unguarded Cells in the Grid
// https://leetcode.com/problems/count-unguarded-cells-in-the-grid/

/**
 * @param {number} m
 * @param {number} n
 * @param {number[][]} guards
 * @param {number[][]} walls
 * @return {number}
 */
var countUnguarded = function(m, n, guards, walls) {
    const grid = Array.from({length: m}, () => new Array(n).fill(0));
    for (const w of walls) grid[w[0]][w[1]] = 2;
    for (const g of guards) grid[g[0]][g[1]] = 2;
    const dirs = [[1,0],[-1,0],[0,1],[0,-1]];
    for (const g of guards) {
        for (const d of dirs) {
            let r = g[0] + d[0], c = g[1] + d[1];
            while (r >= 0 && r < m && c >= 0 && c < n && grid[r][c] !== 2) {
                grid[r][c] = 1;
                r += d[0]; c += d[1];
            }
        }
    }
    let ans = 0;
    for (let i = 0; i < m; i++)
        for (let j = 0; j < n; j++)
            if (grid[i][j] === 0) ans++;
    return ans;
};
