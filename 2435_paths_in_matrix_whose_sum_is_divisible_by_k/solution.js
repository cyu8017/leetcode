// LeetCode 2435 - Paths in Matrix Whose Sum Is Divisible by K
// https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

/**
 * @param {number[][]} grid
 * @param {number} k
 * @return {number}
 */
var numberOfPaths = function(grid, k) {
    const mod = 1000000007;
    const m = grid.length, n = grid[0].length;
    const dp = Array.from({ length: m }, () => Array.from({ length: n }, () => Array(k).fill(0)));
    dp[0][0][grid[0][0] % k] = 1;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            for (let r = 0; r < k; r++) {
                if (dp[i][j][r] === 0) continue;
                if (i + 1 < m) {
                    const nr = (r + grid[i + 1][j]) % k;
                    dp[i + 1][j][nr] = (dp[i + 1][j][nr] + dp[i][j][r]) % mod;
                }
                if (j + 1 < n) {
                    const nr = (r + grid[i][j + 1]) % k;
                    dp[i][j + 1][nr] = (dp[i][j + 1][nr] + dp[i][j][r]) % mod;
                }
            }
        }
    }
    return dp[m - 1][n - 1][0];
};
