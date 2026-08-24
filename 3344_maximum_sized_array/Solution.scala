// LeetCode 3344 - Maximum Sized Array
// https://leetcode.com/problems/maximum-sized-array/

object Solution {
  private def ok(n: Long, s: Long): Boolean = {
    var sum = 0L
    var i = 0L
    while (i < n) {
      var j = 0L
      while (j < n) {
        val ij = i | j
        sum += ij * (n - 1) * n / 2
        if (sum > s) return false
        j += 1
      }
      i += 1
    }
    sum <= s
  }

  def maxSizedArray(s: Long): Int = {
    var lo = 1L
    var hi = 2000L
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (ok(mid, s)) lo = mid
      else hi = mid - 1
    }
    lo.toInt
  }
}
