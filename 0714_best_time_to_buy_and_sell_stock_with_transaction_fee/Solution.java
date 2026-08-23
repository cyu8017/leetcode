// LeetCode 0714 - Best Time to Buy and Sell Stock with Transaction Fee
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution {
    public int maxProfit(int[] prices, int fee) {
        int hold = -prices[0], cash = 0;
        for (int i = 1; i < prices.length; i++) {
            int price = prices[i];
            hold = Math.max(hold, cash - price);
            cash = Math.max(cash, hold + price - fee);
        }
        return cash;
    }
}
