// LeetCode 3473 - Sum of K Subarrays With Length at Least M
// https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/

import java.util.Arrays;

class Solution {
    public long maxSum(int[] nums, int k, int m) {
        int n = nums.length;
        long[] pref = new long[n + 1];
        for (int i = 0; i < n; i++) pref[i + 1] = pref[i] + nums[i];
        final long neg = -(1L << 60);
        long[][] dp = new long[k + 1][n + 1];
        for (int t = 0; t <= k; t++) Arrays.fill(dp[t], neg);
        for (int i = 0; i <= n; i++) dp[0][i] = 0;
        for (int t = 1; t <= k; t++) {
            long best = neg;
            for (int i = t * m; i <= n; i++) {
                int j = i - m;
                best = Math.max(best, dp[t - 1][j] - pref[j]);
                dp[t][i] = best + pref[i];
            }
            for (int i = 1; i <= n; i++) dp[t][i] = Math.max(dp[t][i], dp[t][i - 1]);
        }
        return dp[k][n];
    }
}
