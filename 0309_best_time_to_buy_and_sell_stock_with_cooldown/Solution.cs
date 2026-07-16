// LeetCode 0309 - Best Time to Buy and Sell Stock with Cooldown
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

public class Solution {
    public int MaxProfit(int[] prices) {
        if (prices.Length == 0) {
            return 0;
        }
        int free = 0;
        int hold = -prices[0];
        int cooldown = 0;
        for (int index = 1; index < prices.Length; index++) {
            int price = prices[index];
            int nextFree = System.Math.Max(free, cooldown);
            int nextHold = System.Math.Max(hold, free - price);
            int nextCooldown = hold + price;
            free = nextFree;
            hold = nextHold;
            cooldown = nextCooldown;
        }
        return System.Math.Max(free, cooldown);
    }
}
