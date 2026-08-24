// LeetCode 2969 - Minimum Number of Coins for Fruits II
// https://leetcode.com/problems/minimum-number-of-coins-for-fruits-ii/

object Solution {
  def minimumCoins(prices: Array[Int]): Int = {
    val n = prices.length
    val dp = Array.fill(n + 1)(1 << 30)
    dp(0) = 0
    var i = 1
    while (i <= n) {
      var j = i
      while (j <= n && j <= 2 * i) {
        dp(j) = math.min(dp(j), dp(i - 1) + prices(i - 1))
        j += 1
      }
      i += 1
    }
    dp(n)
  }
}
