// LeetCode 1937 - Maximum Number of Points with Cost
// https://leetcode.com/problems/maximum-number-of-points-with-cost/

class Solution {
    public long maxPoints(int[][] points) {
        int m = points.length, n = points[0].length;
        long[] dp = new long[n];
        for (int c = 0; c < n; c++) dp[c] = points[0][c];
        for (int r = 1; r < m; r++) {
            long[] left = new long[n], right = new long[n], ndp = new long[n];
            left[0] = dp[0];
            for (int c = 1; c < n; c++) left[c] = Math.max(left[c - 1] - 1, dp[c]);
            right[n - 1] = dp[n - 1];
            for (int c = n - 2; c >= 0; c--) right[c] = Math.max(right[c + 1] - 1, dp[c]);
            for (int c = 0; c < n; c++) ndp[c] = points[r][c] + Math.max(left[c], right[c]);
            dp = ndp;
        }
        long ans = Long.MIN_VALUE;
        for (long x : dp) ans = Math.max(ans, x);
        return ans;
    }
}
