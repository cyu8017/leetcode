// LeetCode 0121 - Best Time to Buy and Sell Stock
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

object Solution {
  def maxProfit(prices: Array[Int]): Int = {
    var minPrice = Int.MaxValue
    var best = 0
    for (price <- prices) {
      minPrice = Math.min(minPrice, price)
      best = Math.max(best, price - minPrice)
    }
    best
  }
}