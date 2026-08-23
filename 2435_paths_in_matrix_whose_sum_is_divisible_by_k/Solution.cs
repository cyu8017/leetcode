// LeetCode 2435 - Paths in Matrix Whose Sum Is Divisible by K
// https://leetcode.com/problems/paths-in-matrix-whose-sum-is-divisible-by-k/

public class Solution {
    public int NumberOfPaths(int[][] grid, int k) {
        const int mod = 1000000007;
        int m = grid.Length, n = grid[0].Length;
        int[][][] dp = new int[m][][];
        for (int i = 0; i < m; i++) {
            dp[i] = new int[n][];
            for (int j = 0; j < n; j++) dp[i][j] = new int[k];
        }
        dp[0][0][grid[0][0] % k] = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int r = 0; r < k; r++) {
                    if (dp[i][j][r] == 0) continue;
                    if (i + 1 < m) {
                        int nr = (r + grid[i + 1][j]) % k;
                        dp[i + 1][j][nr] = (dp[i + 1][j][nr] + dp[i][j][r]) % mod;
                    }
                    if (j + 1 < n) {
                        int nr = (r + grid[i][j + 1]) % k;
                        dp[i][j + 1][nr] = (dp[i][j + 1][nr] + dp[i][j][r]) % mod;
                    }
                }
            }
        }
        return dp[m - 1][n - 1][0];
    }
}
