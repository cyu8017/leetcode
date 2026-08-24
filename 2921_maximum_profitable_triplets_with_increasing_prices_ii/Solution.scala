// LeetCode 2921 - Maximum Profitable Triplets With Increasing Prices II
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-ii/

object Solution {
  private var bit: Array[Int] = _

  def maxProfit(prices: Array[Int], profits: Array[Int]): Int = {
    val n = prices.length
    var ans = -1
    val maxLeft = Array.fill(n)(0)
    bit = Array.fill(5002)(0)
    for (j <- 0 until n) {
      maxLeft(j) = query(prices(j) - 1)
      update(prices(j), profits(j))
    }
    for (j <- 0 until n) {
      var bestR = -1
      for (k <- j + 1 until n if prices(k) > prices(j) && profits(k) > bestR) bestR = profits(k)
      if (maxLeft(j) >= 0 && bestR >= 0) {
        val cand = maxLeft(j) + profits(j) + bestR
        if (cand > ans) ans = cand
      }
    }
    ans
  }

  private def update(i0: Int, value: Int): Unit = {
    var i = i0
    while (i < bit.length) {
      if (value > bit(i)) bit(i) = value
      i += i & -i
    }
  }

  private def query(i0: Int): Int = {
    var best = -1
    var i = i0
    while (i > 0) {
      if (bit(i) > best) best = bit(i)
      i -= i & -i
    }
    best
  }
}
