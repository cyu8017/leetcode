// LeetCode 3505 - Minimum Operations to Make Elements Within K Subarrays Equal
// https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

import java.util.Arrays;

class Solution {
    public long minOperations(int[] nums, int x, int k) {
        int n = nums.length;
        long[] minOps = new long[n - x + 1];
        for (int i = 0; i + x <= n; i++) {
            int[] w = new int[x];
            System.arraycopy(nums, i, w, 0, x);
            Arrays.sort(w);
            int med = w[(x - 1) / 2];
            long ops = 0;
            for (int v : w) ops += Math.abs(v - med);
            minOps[i] = ops;
        }
        final long Inf = 1L << 62;
        long[][] dp = new long[n + 1][];
        for (int i = 0; i <= n; i++) {
            dp[i] = new long[k + 1];
            for (int j = 0; j <= k; j++) dp[i][j] = Inf;
        }
        dp[n][0] = 0;
        for (int i = n - 1; i >= 0; i--) {
            for (int j = 0; j <= k; j++) {
                dp[i][j] = dp[i + 1][j];
                if (j > 0 && i + x <= n && minOps[i] + dp[i + x][j - 1] < dp[i][j])
                    dp[i][j] = minOps[i] + dp[i + x][j - 1];
            }
        }
        return dp[0][k];
    }
}
