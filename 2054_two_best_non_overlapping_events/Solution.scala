// LeetCode 2054 - Two Best Non-Overlapping Events
// https://leetcode.com/problems/two-best-non-overlapping-events/

object Solution {
  def maxTwoEvents(events: Array[Array[Int]]): Int = {
    val sorted = events.sortBy(_(0))
    val n = sorted.length
    val suffix = Array.ofDim[Int](n + 1)
    var i = n - 1
    while (i >= 0) {
      suffix(i) = math.max(suffix(i + 1), sorted(i)(2))
      i -= 1
    }
    var ans = 0
    i = 0
    while (i < n) {
      ans = math.max(ans, sorted(i)(2))
      var lo = i + 1
      var hi = n
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (sorted(mid)(0) > sorted(i)(1)) hi = mid
        else lo = mid + 1
      }
      if (lo < n) ans = math.max(ans, sorted(i)(2) + suffix(lo))
      i += 1
    }
    ans
  }
}
