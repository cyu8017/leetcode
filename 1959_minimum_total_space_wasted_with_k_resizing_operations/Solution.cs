// LeetCode 1959 - Minimum Total Space Wasted With K Resizing Operations
// https://leetcode.com/problems/minimum-total-space-wasted-with-k-resizing-operations/

using System;

public class Solution {
    public int MinSpaceWastedKResizing(int[] nums, int k) {
        int n = nums.Length;
        long INF = long.MaxValue / 4;
        var waste = new long[n][];
        for (int i = 0; i < n; i++) {
            waste[i] = new long[n];
            long mx = 0, total = 0;
            for (int j = i; j < n; j++) {
                mx = Math.Max(mx, nums[j]);
                total += nums[j];
                waste[i][j] = mx * (j - i + 1) - total;
            }
        }
        int segments = k + 1;
        var dp = new long[n + 1][];
        for (int i = 0; i <= n; i++) {
            dp[i] = new long[segments + 1];
            Array.Fill(dp[i], INF);
        }
        dp[0][0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int s = 1; s <= Math.Min(segments, i); s++) {
                for (int p = s - 1; p < i; p++)
                    dp[i][s] = Math.Min(dp[i][s], dp[p][s - 1] + waste[p][i - 1]);
            }
        }
        long ans = INF;
        for (int s = 1; s <= segments; s++) ans = Math.Min(ans, dp[n][s]);
        return (int)ans;
    }
}