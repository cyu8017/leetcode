// LeetCode 0813 - Largest Sum of Averages
// https://leetcode.com/problems/largest-sum-of-averages/

using System;

public class Solution {
    public double LargestSumOfAverages(int[] nums, int k) {
        int n = nums.Length;
        double[] prefix = new double[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
        double Average(int i, int j) => (prefix[j] - prefix[i]) / (j - i);
        double[] dp = new double[n];
        for (int i = 0; i < n; i++) dp[i] = Average(0, i + 1);
        for (int groups = 2; groups <= k; groups++) {
            double[] nxt = new double[n];
            for (int i = groups - 1; i < n; i++) {
                double best = 0.0;
                for (int j = groups - 2; j < i; j++) best = Math.Max(best, dp[j] + Average(j + 1, i + 1));
                nxt[i] = best;
            }
            dp = nxt;
        }
        return dp[n - 1];
    }
}
