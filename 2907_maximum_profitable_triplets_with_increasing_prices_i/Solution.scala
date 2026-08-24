// LeetCode 2907 - Maximum Profitable Triplets With Increasing Prices I
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-i/

object Solution {
  def maxProfit(prices: Array[Int], profits: Array[Int]): Int = {
    val n = prices.length
    var ans = -1
    for (j <- 0 until n) {
      var bestL = -1
      var bestR = -1
      for (i <- 0 until j if prices(i) < prices(j) && profits(i) > bestL) bestL = profits(i)
      for (k <- j + 1 until n if prices(k) > prices(j) && profits(k) > bestR) bestR = profits(k)
      if (bestL >= 0 && bestR >= 0) {
        val cand = bestL + profits(j) + bestR
        if (cand > ans) ans = cand
      }
    }
    ans
  }
}
