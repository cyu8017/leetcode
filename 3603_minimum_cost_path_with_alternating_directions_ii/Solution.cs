// LeetCode 3603 - Minimum Cost Path with Alternating Directions II
// https://leetcode.com/problems/minimum-cost-path-with-alternating-directions-ii/

using System;

public class Solution {
    public long MinCost(int m, int n, int[][] waitCost) {
        long[][] dp = new long[m][];
        for (int i = 0; i < m; i++) {
            dp[i] = new long[n];
            for (int j = 0; j < n; j++) dp[i][j] = long.MaxValue / 4;
        }
        long Entry(int i, int j) => 1L * (i + 1) * (j + 1);
        dp[0][0] = Entry(0, 0);
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                if (i > 0) {
                    long cand = dp[i - 1][j] + Entry(i, j);
                    if (!(i - 1 == 0 && j == 0)) cand += waitCost[i - 1][j];
                    dp[i][j] = Math.Min(dp[i][j], cand);
                }
                if (j > 0) {
                    long cand = dp[i][j - 1] + Entry(i, j);
                    if (!(i == 0 && j - 1 == 0)) cand += waitCost[i][j - 1];
                    dp[i][j] = Math.Min(dp[i][j], cand);
                }
            }
        }
        return dp[m - 1][n - 1];
    }
}
