// LeetCode 3473 - Sum of K Subarrays With Length at Least M
// https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/

using System;

public class Solution {
    public long MaxSum(int[] nums, int k, int m) {
        int n = nums.Length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
        const long neg = -1L << 60;
        long[][] dp = new long[k + 1][];
        for (int t = 0; t <= k; t++) {
            dp[t] = new long[n + 1];
            for (int i = 0; i <= n; i++) dp[t][i] = neg;
        }
        for (int i = 0; i <= n; i++) dp[0][i] = 0;
        for (int t = 1; t <= k; t++) {
            long best = neg;
            for (int i = t * m; i <= n; i++) {
                int j = i - m;
                best = Math.Max(best, dp[t - 1][j] - pref[j]);
                dp[t][i] = best + pref[i];
            }
            for (int i = 1; i <= n; i++) dp[t][i] = Math.Max(dp[t][i], dp[t][i - 1]);
        }
        return dp[k][n];
    }
}
