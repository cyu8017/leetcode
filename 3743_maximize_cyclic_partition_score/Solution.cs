// LeetCode 3743 - Maximize Cyclic Partition Score
// https://leetcode.com/problems/maximize-cyclic-partition-score/

using System.Collections.Generic;

public class Solution {
    public long MaximumScore(int[] nums, int k) {
        int n = nums.Length;
        var a = new List<int>(nums);
        a.AddRange(nums);
        if (k > n) k = n;
        long best = 0;
        const long NEG = -(1L << 60);
        for (int start = 0; start < n; start++) {
            int[] seg = new int[n];
            for (int i = 0; i < n; i++) seg[i] = a[start + i];
            long[,] dp = new long[n + 1, k + 1];
            for (int i = 0; i <= n; i++)
                for (int j = 0; j <= k; j++)
                    dp[i, j] = NEG;
            dp[0, 0] = 0;
            for (int i = 1; i <= n; i++) {
                for (int j = 1; j <= k && j <= i; j++) {
                    long mx = NEG;
                    for (int t = i; t >= j; t--) {
                        if (seg[t - 1] > mx) mx = seg[t - 1];
                        if (dp[t - 1, j - 1] > NEG) {
                            long cand = dp[t - 1, j - 1] + mx;
                            if (cand > dp[i, j]) dp[i, j] = cand;
                        }
                    }
                }
            }
            if (dp[n, k] > best) best = dp[n, k];
        }
        return best;
    }
}
