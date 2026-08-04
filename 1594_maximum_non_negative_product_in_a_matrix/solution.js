// LeetCode 1594 - Maximum Non Negative Product in a Matrix
// https://leetcode.com/problems/maximum-non-negative-product-in-a-matrix/

/**
 * @param {number[][]} grid
 * @return {number}
 */
var maxProductPath = function(grid) {
    const MOD = 1000000007;
    const m = grid.length, n = grid[0].length;
    const high = Array.from({ length: m }, () => Array(n).fill(0));
    const low = Array.from({ length: m }, () => Array(n).fill(0));
    high[0][0] = low[0][0] = grid[0][0];
    for (let r = 0; r < m; r++) {
        for (let c = 0; c < n; c++) {
            if (r === 0 && c === 0) continue;
            const values = [];
            if (r) {
                values.push(high[r - 1][c] * grid[r][c], low[r - 1][c] * grid[r][c]);
            }
            if (c) {
                values.push(high[r][c - 1] * grid[r][c], low[r][c - 1] * grid[r][c]);
            }
            high[r][c] = Math.max(...values);
            low[r][c] = Math.min(...values);
        }
    }
    const ans = high[m - 1][n - 1];
    return ans >= 0 ? ((ans % MOD) + MOD) % MOD : -1;
};
