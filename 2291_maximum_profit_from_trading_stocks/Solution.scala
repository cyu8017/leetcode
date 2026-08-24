// LeetCode 2291 - Maximum Profit From Trading Stocks
// https://leetcode.com/problems/maximum-profit-from-trading-stocks/

object Solution {
  def maximumProfit(present: Array[Int], future: Array[Int], budget: Int): Int = {
    val n = present.length
    val dp = new Array[Int](budget + 1)
    var i = 0
    while (i < n) {
      val profit = future(i) - present(i)
      if (profit > 0) {
        val cost = present(i)
        var b = budget
        while (b >= cost) {
          dp(b) = math.max(dp(b), dp(b - cost) + profit)
          b -= 1
        }
      }
      i += 1
    }
    dp(budget)
  }
}
