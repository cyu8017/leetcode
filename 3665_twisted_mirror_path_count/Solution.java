// LeetCode 3665 - Twisted Mirror Path Count
// https://leetcode.com/problems/twisted-mirror-path-count/

class Solution {
    private int m, n;
    private int[][] grid;

    private int[] nextCell(int i, int j, int di, int dj) {
        int ni = i + di, nj = j + dj;
        while (ni >= 0 && nj >= 0 && ni < m && nj < n && grid[ni][nj] == 1) {
            if (dj == 1) {
                di = 1;
                dj = 0;
            } else {
                di = 0;
                dj = 1;
            }
            ni += di;
            nj += dj;
        }
        if (ni < 0 || nj < 0 || ni >= m || nj >= n) return null;
        return new int[] {ni, nj};
    }

    public int uniquePaths(int[][] grid) {
        final int MOD = 1_000_000_007;
        this.grid = grid;
        m = grid.length;
        n = grid[0].length;
        int[][] dp = new int[m][n];
        if (grid[0][0] == 1) return 0;
        dp[0][0] = 1;
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (grid[i][j] == 1 || dp[i][j] == 0) continue;
                int[] a = nextCell(i, j, 0, 1);
                if (a != null) dp[a[0]][a[1]] = (dp[a[0]][a[1]] + dp[i][j]) % MOD;
                int[] b = nextCell(i, j, 1, 0);
                if (b != null) dp[b[0]][b[1]] = (dp[b[0]][b[1]] + dp[i][j]) % MOD;
            }
        }
        return dp[m - 1][n - 1];
    }
}
