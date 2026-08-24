// LeetCode 3393 - Count Paths With the Given XOR Value
// https://leetcode.com/problems/count-paths-with-the-given-xor-value/

export function countPathsWithXorValue(grid: any, k: any): any {
    const mod = 1000000007;
    const m = grid.length, n = grid[0].length;
    const dp = Array.from({length: m}, () =>
        Array.from({length: n}, () => new Array(16).fill(0)));
    dp[0][0][grid[0][0]] = 1;
    for (let i = 0; i < m; i++) {
        for (let j = 0; j < n; j++) {
            for (let x = 0; x < 16; x++) {
                if (dp[i][j][x] === 0) continue;
                if (i + 1 < m) {
                    const nx = x ^ grid[i + 1][j];
                    dp[i + 1][j][nx] = (dp[i + 1][j][nx] + dp[i][j][x]) % mod;
                }
                if (j + 1 < n) {
                    const nx = x ^ grid[i][j + 1];
                    dp[i][j + 1][nx] = (dp[i][j + 1][nx] + dp[i][j][x]) % mod;
                }
            }
        }
    }
    return dp[m - 1][n - 1][k];
}
