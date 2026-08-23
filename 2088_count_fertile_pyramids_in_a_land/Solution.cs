// LeetCode 2088 - Count Fertile Pyramids in a Land
// https://leetcode.com/problems/count-fertile-pyramids-in-a-land/

public class Solution {
    private int Count(int[][] g) {
        int m = g.Length, n = g[0].Length;
        int[][] dp = new int[m][];
        for (int i = 0; i < m; i++) {
            dp[i] = new int[n];
            for (int j = 0; j < n; j++) dp[i][j] = g[i][j];
        }
        int ans = 0;
        for (int i = m - 2; i >= 0; i--) {
            for (int j = 1; j < n - 1; j++) {
                if (g[i][j] == 1) {
                    dp[i][j] = 1 + Math.Min(dp[i + 1][j - 1], Math.Min(dp[i + 1][j], dp[i + 1][j + 1]));
                    ans += dp[i][j] - 1;
                }
            }
        }
        return ans;
    }

    public int CountPyramids(int[][] grid) {
        int ans = Count(grid);
        int m = grid.Length;
        int[][] rev = new int[m][];
        for (int i = 0; i < m; i++) rev[i] = grid[m - 1 - i];
        return ans + Count(rev);
    }
}
