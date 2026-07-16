// LeetCode 0123 - Best Time to Buy and Sell Stock III
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/

class Solution {
    fun maxProfit(prices: IntArray): Int {
        var buy1 = Int.MAX_VALUE
        var buy2 = Int.MAX_VALUE
        var sell1 = 0
        var sell2 = 0
        for (price in prices) {
            buy1 = minOf(buy1, price)
            sell1 = maxOf(sell1, price - buy1)
            buy2 = minOf(buy2, price - sell1)
            sell2 = maxOf(sell2, price - buy2)
        }
        return sell2
    }
}