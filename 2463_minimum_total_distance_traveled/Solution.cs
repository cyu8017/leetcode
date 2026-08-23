// LeetCode 2463 - Minimum Total Distance Traveled
// https://leetcode.com/problems/minimum-total-distance-traveled/

using System;
using System.Collections.Generic;

public class Solution {
    public long MinimumTotalDistance(IList<int> robot, int[][] factory) {
        var robots = new List<int>(robot);
        robots.Sort();
        Array.Sort(factory, (a, b) => a[0].CompareTo(b[0]));
        int m = robots.Count;
        var pos = new List<int>();
        foreach (var f in factory) {
            for (int c = 0; c < f[1]; c++) pos.Add(f[0]);
        }
        int n = pos.Count;
        const long INF = 1L << 60;
        long[][] dp = new long[m + 1][];
        for (int i = 0; i <= m; i++) {
            dp[i] = new long[n + 1];
            for (int j = 0; j <= n; j++) dp[i][j] = INF;
        }
        for (int j = 0; j <= n; j++) dp[0][j] = 0;
        for (int i = 1; i <= m; i++) {
            for (int j = i; j <= n; j++) {
                dp[i][j] = dp[i][j - 1];
                long diff = robots[i - 1] - pos[j - 1];
                if (diff < 0) diff = -diff;
                if (dp[i - 1][j - 1] + diff < dp[i][j]) dp[i][j] = dp[i - 1][j - 1] + diff;
            }
        }
        return dp[m][n];
    }
}
