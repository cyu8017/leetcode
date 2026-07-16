// LeetCode 0122 - Best Time to Buy and Sell Stock II
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

object Solution {
  def maxProfit(prices: Array[Int]): Int = {
    var profit = 0
    for (i <- 1 until prices.length) {
      if (prices(i) > prices(i - 1)) profit += prices(i) - prices(i - 1)
    }
    profit
  }
}