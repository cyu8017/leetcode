// LeetCode 3652 - Best Time to Buy and Sell Stock using Strategy
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/

using System;

public class Solution {
    public long MaxProfit(int[] prices, int[] strategy, int k) {
        int n = prices.Length;
        long[] s = new long[n + 1], t = new long[n + 1];
        for (int i = 1; i <= n; i++) {
            s[i] = s[i - 1] + 1L * prices[i - 1] * strategy[i - 1];
            t[i] = t[i - 1] + prices[i - 1];
        }
        long ans = s[n];
        for (int i = k; i <= n; i++) ans = Math.Max(ans, s[n] - (s[i] - s[i - k]) + (t[i] - t[i - k / 2]));
        return ans;
    }
}
