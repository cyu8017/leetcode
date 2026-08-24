// LeetCode 0714 - Best Time to Buy and Sell Stock with Transaction Fee
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution {
    fun maxProfit(prices: IntArray, fee: Int): Int {
        var hold = -prices[0]
        var cash = 0
        for (i in 1 until prices.size) {
            var price = prices[i]
            hold = maxOf(hold, cash - price)
            cash = maxOf(cash, hold + price - fee)
        }
        return cash
    }
}
