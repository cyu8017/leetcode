// LeetCode 1751 - Maximum Number of Events That Can Be Attended II
// https://leetcode.com/problems/maximum-number-of-events-that-can-be-attended-ii/

object Solution {
  def maxValue(events: Array[Array[Int]], k: Int): Int = {
    val sorted = events.sortBy(e => (e(0), e(1), e(2)))
    val n = sorted.length
    val starts = sorted.map(_(0))

    def upperBound(target: Int): Int = {
      var lo = 0
      var hi = n
      while (lo < hi) {
        val mid = (lo + hi) >>> 1
        if (starts(mid) <= target) lo = mid + 1
        else hi = mid
      }
      lo
    }

    val dp = Array.ofDim[Int](k + 1, n + 1)
    for (i <- (n - 1) to 0 by -1) {
      val j = upperBound(sorted(i)(1))
      for (remain <- 1 to k) {
        dp(remain)(i) = math.max(dp(remain)(i + 1), sorted(i)(2) + dp(remain - 1)(j))
      }
    }
    dp(k)(0)
  }
}
