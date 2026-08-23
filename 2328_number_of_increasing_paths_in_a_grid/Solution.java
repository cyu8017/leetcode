// LeetCode 2328 - Number of Increasing Paths in a Grid
// https://leetcode.com/problems/number-of-increasing-paths-in-a-grid/

class Solution {
    private static final int MOD = 1_000_000_007;
    private int[][] grid, dp;
    private int m, n;
    private final int[][] dirs = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

    public int countPaths(int[][] grid) {
        this.grid = grid;
        m = grid.length;
        n = grid[0].length;
        dp = new int[m][n];
        int ans = 0;
        for (int i = 0; i < m; ++i)
            for (int j = 0; j < n; ++j)
                ans = (ans + dfs(i, j)) % MOD;
        return ans;
    }

    private int dfs(int r, int c) {
        if (dp[r][c] != 0) return dp[r][c];
        int res = 1;
        for (int[] d : dirs) {
            int nr = r + d[0], nc = c + d[1];
            if (nr >= 0 && nr < m && nc >= 0 && nc < n && grid[nr][nc] > grid[r][c])
                res = (res + dfs(nr, nc)) % MOD;
        }
        return dp[r][c] = res;
    }
}
