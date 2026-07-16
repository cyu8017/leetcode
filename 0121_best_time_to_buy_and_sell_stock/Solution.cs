// LeetCode 0121 - Best Time to Buy and Sell Stock
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

public class Solution {
    public int MaxProfit(int[] prices) {
        int minPrice = int.MaxValue, best = 0;
        foreach (int price in prices) {
            minPrice = System.Math.Min(minPrice, price);
            best = System.Math.Max(best, price - minPrice);
        }
        return best;
    }
}