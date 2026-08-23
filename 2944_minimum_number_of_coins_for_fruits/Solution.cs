// LeetCode 2944 - Minimum Number of Coins for Fruits
// https://leetcode.com/problems/minimum-number-of-coins-for-fruits/

public class Solution {
    public int MinimumCoins(int[] prices) {
        int n = prices.Length;
        int[] dp = new int[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = 1 << 30;
        dp[0] = 0;
        for (int i = 1; i <= n; i++)
            for (int j = i; j <= n && j <= i + i; j++) {
                int cand = dp[i - 1] + prices[i - 1];
                if (cand < dp[j]) dp[j] = cand;
            }
        return dp[n];
    }
}
