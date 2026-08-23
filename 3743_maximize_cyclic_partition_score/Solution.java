// LeetCode 3743 - Maximize Cyclic Partition Score
// https://leetcode.com/problems/maximize_cyclic_partition_score/

import java.util.Arrays;

class Solution {
    public long maximumScore(int[] nums, int k) {
        int n = nums.length;
        int[] a = new int[n * 2];
        System.arraycopy(nums, 0, a, 0, n);
        System.arraycopy(nums, 0, a, n, n);
        if (k > n) k = n;
        long best = 0;
        final long NEG = -(1L << 60);
        for (int start = 0; start < n; start++) {
            int[] seg = Arrays.copyOfRange(a, start, start + n);
            long[][] dp = new long[n + 1][k + 1];
            for (int i = 0; i <= n; i++) Arrays.fill(dp[i], NEG);
            dp[0][0] = 0;
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= k && j <= i; j++) {
                    long mx = NEG;
                    for (int t = i; t >= j; t--) {
                        if (seg[t - 1] > mx) mx = seg[t - 1];
                        if (dp[t - 1][j - 1] > NEG) {
                            long cand = dp[t - 1][j - 1] + mx;
                            if (cand > dp[i][j]) dp[i][j] = cand;
                        }
                    }
                }
            }
            if (dp[n][k] > best) best = dp[n][k];
        }
        return best;
    }
}
