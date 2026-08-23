// LeetCode 3418 - Maximum Amount of Money Robot Can Earn
// https://leetcode.com/problems/maximum-amount-of-money-robot-can-earn/

using System;

public class Solution {
    public int MaximumAmount(int[][] coins) {
        int m = coins.Length, n = coins[0].Length;
        const int neg = -(1 << 30);
        int[][][] dp = new int[m][][];
        for (int i = 0; i < m; i++) {
            dp[i] = new int[n][];
            for (int j = 0; j < n; j++) {
                dp[i][j] = new int[3];
                for (int k = 0; k < 3; k++) dp[i][j][k] = neg;
            }
        }
        if (coins[0][0] < 0) {
            dp[0][0][0] = coins[0][0];
            dp[0][0][1] = 0;
            dp[0][0][2] = 0;
        } else {
            dp[0][0][0] = coins[0][0];
            dp[0][0][1] = coins[0][0];
            dp[0][0][2] = coins[0][0];
        }
        for (int i = 0; i < m; i++) {
            for (int j = 0; j < n; j++) {
                if (i == 0 && j == 0) continue;
                for (int k = 0; k < 3; k++) {
                    int best = neg;
                    if (i > 0) best = Math.Max(best, dp[i - 1][j][k]);
                    if (j > 0) best = Math.Max(best, dp[i][j - 1][k]);
                    if (best == neg) continue;
                    if (coins[i][j] >= 0) dp[i][j][k] = best + coins[i][j];
                    else dp[i][j][k] = Math.Max(dp[i][j][k], best + coins[i][j]);
                }
                for (int k = 1; k < 3; k++) {
                    int best = neg;
                    if (i > 0) best = Math.Max(best, dp[i - 1][j][k - 1]);
                    if (j > 0) best = Math.Max(best, dp[i][j - 1][k - 1]);
                    if (best != neg && coins[i][j] < 0) dp[i][j][k] = Math.Max(dp[i][j][k], best);
                }
            }
        }
        return Math.Max(dp[m - 1][n - 1][0], Math.Max(dp[m - 1][n - 1][1], dp[m - 1][n - 1][2]));
    }
}
