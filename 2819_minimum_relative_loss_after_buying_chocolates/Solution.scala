// LeetCode 2819 - Minimum Relative Loss After Buying Chocolates
// https://leetcode.com/problems/minimum-relative-loss-after-buying-chocolates/

object Solution {
  def minimumRelativeLosses(prices: Array[Int], queries: Array[Array[Int]]): Array[Long] = {
    java.util.Arrays.sort(prices)
    val n = prices.length
    val ans = Array.ofDim[Long](queries.length)
    var qi = 0
    while (qi < queries.length) {
      val kk = queries(qi)(0)
      val m = queries(qi)(1)
      val losses = Array.tabulate(n) { i =>
        if (prices(i) <= kk) prices(i).toLong else 2L * kk - prices(i)
      }
      java.util.Arrays.sort(losses)
      var sum = 0L
      var i = 0
      while (i < m) {
        sum += losses(i)
        i += 1
      }
      ans(qi) = sum
      qi += 1
    }
    ans
  }
}
