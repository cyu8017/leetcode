// LeetCode 2008 - Maximum Earnings From Taxi
// https://leetcode.com/problems/maximum-earnings-from-taxi/

object Solution {
  def maxTaxiEarnings(n: Int, rides: Array[Array[Int]]): Long = {
    val sorted = rides.sortBy(_(1))
    val m = sorted.length
    val ends = sorted.map(_(1))
    val dp = Array.ofDim[Long](m + 1)
    var i = 0
    while (i < m) {
      val start = sorted(i)(0)
      val end = sorted(i)(1)
      val tip = sorted(i)(2)
      val earn = end.toLong - start + tip
      var lo = 0
      var hi = m
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (ends(mid) <= start) lo = mid + 1
        else hi = mid
      }
      dp(i + 1) = math.max(dp(i), earn + dp(lo))
      i += 1
    }
    dp(m)
  }
}
