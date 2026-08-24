// LeetCode 3573 - Best Time to Buy and Sell Stock V
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/

object Solution {
  def maximumProfit(prices: Array[Int], k: Int): Long = {
    val n = prices.length
    val f = Array.ofDim[Long](n, k + 1, 3)
    var j = 1
    while (j <= k) {
      f(0)(j)(1) = -prices(0)
      f(0)(j)(2) = prices(0)
      j += 1
    }
    var i = 1
    while (i < n) {
      j = 1
      while (j <= k) {
        f(i)(j)(0) = math.max(f(i - 1)(j)(0), math.max(f(i - 1)(j)(1) + prices(i), f(i - 1)(j)(2) - prices(i)))
        f(i)(j)(1) = math.max(f(i - 1)(j)(1), f(i - 1)(j - 1)(0) - prices(i))
        f(i)(j)(2) = math.max(f(i - 1)(j)(2), f(i - 1)(j - 1)(0) + prices(i))
        j += 1
      }
      i += 1
    }
    f(n - 1)(k)(0)
  }
}
