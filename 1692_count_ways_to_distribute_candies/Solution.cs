// LeetCode 1692 - Count Ways to Distribute Candies
// https://leetcode.com/problems/count-ways-to-distribute-candies/

using System;

public class Solution {
    public int WaysToDistribute(int n, int k) {
        const int MOD = 1_000_000_007;
        long[] dp = new long[k + 1];
        dp[0] = 1;
        for (int i = 1; i <= n; i++) {
            for (int j = Math.Min(i, k); j >= 1; j--) {
                dp[j] = (dp[j - 1] + j * dp[j]) % MOD;
            }
            dp[0] = 0;
        }
        return (int)dp[k];
    }
}
