// LeetCode 0309 - Best Time to Buy and Sell Stock with Cooldown
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length == 0) {
            return 0;
        }
        int free = 0;
        int hold = -prices[0];
        int cooldown = 0;
        for (int index = 1; index < prices.length; index++) {
            int price = prices[index];
            int nextFree = Math.max(free, cooldown);
            int nextHold = Math.max(hold, free - price);
            int nextCooldown = hold + price;
            free = nextFree;
            hold = nextHold;
            cooldown = nextCooldown;
        }
        return Math.max(free, cooldown);
    }
}
