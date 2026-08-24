// LeetCode 0121 - Best Time to Buy and Sell Stock
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution {
    fun maxProfit(prices: IntArray): Int {
        var minPrice = Int.MAX_VALUE
        var best = 0
        for (price in prices) {
            minPrice = minOf(minPrice, price)
            best = maxOf(best, price - minPrice)
        }
        return best
    }
}