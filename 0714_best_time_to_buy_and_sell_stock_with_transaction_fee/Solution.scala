// LeetCode 0714 - Best Time to Buy and Sell Stock with Transaction Fee
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

object Solution {
  def maxProfit(prices: Array[Int], fee: Int): Int = {
    var hold = -prices(0)
    var cash = 0
    var i = 1
    while (i < prices.length) {
      val price = prices(i)
      hold = math.max(hold, cash - price)
      cash = math.max(cash, hold + price - fee)
      i += 1
    }
    cash
  }
}
