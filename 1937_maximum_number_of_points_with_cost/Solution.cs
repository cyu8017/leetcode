// LeetCode 1937 - Maximum Number of Points with Cost
// https://leetcode.com/problems/maximum-number-of-points-with-cost/

using System;

public class Solution {
    public long MaxPoints(int[][] points) {
        int m = points.Length, n = points[0].Length;
        var dp = new long[n];
        for (int c = 0; c < n; c++) dp[c] = points[0][c];
        for (int r = 1; r < m; r++) {
            var left = new long[n];
            var right = new long[n];
            left[0] = dp[0];
            for (int c = 1; c < n; c++) left[c] = Math.Max(left[c - 1] - 1, dp[c]);
            right[n - 1] = dp[n - 1];
            for (int c = n - 2; c >= 0; c--) right[c] = Math.Max(right[c + 1] - 1, dp[c]);
            var ndp = new long[n];
            for (int c = 0; c < n; c++) ndp[c] = points[r][c] + Math.Max(left[c], right[c]);
            dp = ndp;
        }
        long ans = dp[0];
        for (int c = 1; c < n; c++) ans = Math.Max(ans, dp[c]);
        return ans;
    }
}