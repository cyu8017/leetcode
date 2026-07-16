// LeetCode 0123 - Best Time to Buy and Sell Stock III
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

public class Solution {
    public int MaxProfit(int[] prices) {
        int buy1 = int.MaxValue, buy2 = int.MaxValue;
        int sell1 = 0, sell2 = 0;
        foreach (int price in prices) {
            buy1 = System.Math.Min(buy1, price);
            sell1 = System.Math.Max(sell1, price - buy1);
            buy2 = System.Math.Min(buy2, price - sell1);
            sell2 = System.Math.Max(sell2, price - buy2);
        }
        return sell2;
    }
}