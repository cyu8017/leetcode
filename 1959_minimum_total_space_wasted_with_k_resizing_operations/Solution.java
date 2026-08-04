// LeetCode 1959 - Minimum Total Space Wasted With K Resizing Operations
// https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/

import java.util.*;

class Solution {
    public int minSpaceWastedKResizing(int[] nums, int k) {
        int n = nums.length;
        long INF = (long) 1e18;
        long[][] waste = new long[n][n];
        for (int i = 0; i < n; i++) {
            int mx = 0;
            long total = 0;
            for (int j = i; j < n; j++) {
                mx = Math.max(mx, nums[j]);
                total += nums[j];
                waste[i][j] = mx * (j - i + 1L) - total;
            }
        }
        int segments = k + 1;
        long[][] dp = new long[n + 1][segments + 1];
        for (int i = 0; i <= n; i++) Arrays.fill(dp[i], INF);
        dp[0][0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int s = 1; s <= Math.min(segments, i); s++) {
                for (int p = s - 1; p < i; p++) {
                    dp[i][s] = Math.min(dp[i][s], dp[p][s - 1] + waste[p][i - 1]);
                }
            }
        }
        long ans = INF;
        for (int s = 1; s <= segments; s++) ans = Math.min(ans, dp[n][s]);
        return (int) ans;
    }
}
