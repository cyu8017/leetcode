// LeetCode 2291 - Maximum Profit From Trading Stocks
// https://leetcode.com/problems/maximum-profit-from-trading-stocks/

class Solution {
    public int maximumProfit(int[] present, int[] future, int budget) {
        int n = present.length;
        int[] dp = new int[budget + 1];
        for (int i = 0; i < n; i++) {
            int profit = future[i] - present[i];
            if (profit <= 0) continue;
            int cost = present[i];
            for (int b = budget; b >= cost; b--)
                dp[b] = Math.max(dp[b], dp[b - cost] + profit);
        }
        return dp[budget];
    }
}
