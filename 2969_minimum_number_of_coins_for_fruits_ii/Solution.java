// LeetCode 2969 - Minimum Number of Coins for Fruits II
// https://leetcode.com/problems/minimum-number-of-coins-for-fruits-ii/

class Solution {
    public int minimumCoins(int[] prices) {
        int n = prices.length;
        int[] dp = new int[n + 1];
        for (int i = 0; i <= n; i++) dp[i] = 1 << 30;
        dp[0] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = i; j <= n && j <= 2 * i; j++) {
                dp[j] = Math.min(dp[j], dp[i - 1] + prices[i - 1]);
            }
        }
        return dp[n];
    }
}
