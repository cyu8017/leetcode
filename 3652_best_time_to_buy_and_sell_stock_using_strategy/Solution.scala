// LeetCode 3652 - Best Time to Buy and Sell Stock using Strategy
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/

object Solution {
  def maxProfit(prices: Array[Int], strategy: Array[Int], k: Int): Long = {
    val n = prices.length
    val s = new Array[Long](n + 1)
    val t = new Array[Long](n + 1)
    var i = 1
    while (i <= n) {
      s(i) = s(i - 1) + 1L * prices(i - 1) * strategy(i - 1)
      t(i) = t(i - 1) + prices(i - 1)
      i += 1
    }
    var ans = s(n)
    i = k
    while (i <= n) {
      ans = math.max(ans, s(n) - (s(i) - s(i - k)) + (t(i) - t(i - k / 2)))
      i += 1
    }
    ans
  }
}
