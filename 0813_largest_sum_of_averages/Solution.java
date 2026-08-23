// LeetCode 0813 - Largest Sum of Averages
// https://leetcode.com/problems/largest-sum-of-averages/

class Solution {
    public double largestSumOfAverages(int[] nums, int k) {
        int n = nums.length;
        double[] prefix = new double[n + 1];
        for (int i = 0; i < n; i++) prefix[i + 1] = prefix[i] + nums[i];
        double[] dp = new double[n];
        for (int i = 0; i < n; i++) dp[i] = (prefix[i + 1] - prefix[0]) / (i + 1);
        for (int groups = 2; groups <= k; groups++) {
            double[] nxt = new double[n];
            for (int i = groups - 1; i < n; i++) {
                double best = 0.0;
                for (int j = groups - 2; j < i; j++) {
                    best = Math.max(best, dp[j] + (prefix[i + 1] - prefix[j + 1]) / (i - j));
                }
                nxt[i] = best;
            }
            dp = nxt;
        }
        return dp[n - 1];
    }
}
