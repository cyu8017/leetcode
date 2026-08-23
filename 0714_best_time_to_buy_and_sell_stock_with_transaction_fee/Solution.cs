// LeetCode 0714 - Best Time to Buy and Sell Stock with Transaction Fee
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

using System;

public class Solution {
    public int MaxProfit(int[] prices, int fee) {
        int hold = -prices[0], cash = 0;
        for (int i = 1; i < prices.Length; i++) {
            int price = prices[i];
            hold = Math.Max(hold, cash - price);
            cash = Math.Max(cash, hold + price - fee);
        }
        return cash;
    }
}
