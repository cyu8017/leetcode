// LeetCode 3393 - Count Paths With the Given XOR Value
// https://leetcode.com/problems/count-paths-with-the-given-xor-value/

class Solution {
    public int countPathsWithXorValue(int[][] grid, int k) {
        final int mod = 1000000007;
        int m = grid.length, n = grid[0].length;
        int[][][] dp = new int[m][][];
        for (int i = 0; i < m; i++) {
            dp[i] = new int[n][];
            for (int j = 0; j < n; j++) dp[i][j] = new int[16];
        }
        dp[0][0][grid[0][0]] = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                for (int x = 0; x < 16; x++) {
                    if (dp[i][j][x] == 0) continue;
                    if (i + 1 < m) {
                        int nx = x ^ grid[i + 1][j];
                        dp[i + 1][j][nx] = (dp[i + 1][j][nx] + dp[i][j][x]) % mod;
                    }
                    if (j + 1 < n) {
                        int nx = x ^ grid[i][j + 1];
                        dp[i][j + 1][nx] = (dp[i][j + 1][nx] + dp[i][j][x]) % mod;
                    }
                }
            }
        }
        return dp[m - 1][n - 1][k];
    }
}
