// LeetCode 0309 - Best Time to Buy and Sell Stock with Cooldown
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

class Solution {
    fun maxProfit(prices: IntArray): Int {
        if (prices.isEmpty()) {
            return 0
        }
        var free = 0
        var hold = -prices[0]
        var cooldown = 0
        for (index in 1 until prices.size) {
            val price = prices[index]
            val nextFree = maxOf(free, cooldown)
            val nextHold = maxOf(hold, free - price)
            val nextCooldown = hold + price
            free = nextFree
            hold = nextHold
            cooldown = nextCooldown
        }
        return maxOf(free, cooldown)
    }
}
