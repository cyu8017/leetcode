// LeetCode 3989 - Maximum Consistent Columns in a Grid
// https://leetcode.com/problems/maximum-consistent-columns-in-a-grid/

class Solution {
    public int maxConsistentColumns(int[][] grid, int limit) {
        int m = grid.length;
        int n = grid[0].length;
        int[] dp = new int[n];
        int ans = 1;
        for (int j = 0; j < n; j++) {
            dp[j] = 1;
            for (int i = 0; i < j; i++) {
                if (dp[i] + 1 <= dp[j]) continue;
                boolean ok = true;
                for (int r = 0; r < m; r++) {
                    int d = Math.abs(grid[r][j] - grid[r][i]);
                    if (d > limit) { ok = false; break; }
                }
                if (ok) dp[j] = dp[i] + 1;
            }
            if (dp[j] > ans) ans = dp[j];
        }
        return ans;
    }
}
