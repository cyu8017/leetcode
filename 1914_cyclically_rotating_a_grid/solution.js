// LeetCode 1914 - Cyclically Rotating a Grid
// https://leetcode.com/problems/cyclically-rotating-a-grid/

/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number[][]}
 */
var rotateGrid = function(grid, k) {
    const m = grid.length, n = grid[0].length;
    const layers = Math.floor(Math.min(m, n) / 2);
    for (let layer = 0; layer < layers; layer++) {
        const vals = [];
        for (let c = layer; c < n - layer; c++) vals.push(grid[layer][c]);
        for (let r = layer + 1; r < m - layer; r++) vals.push(grid[r][n - layer - 1]);
        if (m - 2 * layer > 1) {
            for (let c = n - layer - 2; c >= layer; c--) vals.push(grid[m - layer - 1][c]);
        }
        if (n - 2 * layer > 1) {
            for (let r = m - layer - 2; r > layer; r--) vals.push(grid[r][layer]);
        }
        const shift = k % vals.length;
        const rotated = vals.slice(shift).concat(vals.slice(0, shift));
        let idx = 0;
        for (let c = layer; c < n - layer; c++) grid[layer][c] = rotated[idx++];
        for (let r = layer + 1; r < m - layer; r++) grid[r][n - layer - 1] = rotated[idx++];
        if (m - 2 * layer > 1) {
            for (let c = n - layer - 2; c >= layer; c--) grid[m - layer - 1][c] = rotated[idx++];
        }
        if (n - 2 * layer > 1) {
            for (let r = m - layer - 2; r > layer; r--) grid[r][layer] = rotated[idx++];
        }
    }
    return grid;
};
