// LeetCode 1891 - Cutting Ribbons
// https://leetcode.com/problems/cutting-ribbons/

object Solution {
  def maxLength(ribbons: Array[Int], k: Int): Int = {
    def can(length: Int): Boolean = {
      var total = 0L
      for (ribbon <- ribbons) {
        total += ribbon / length
        if (total >= k) return true
      }
      total >= k
    }

    var lo = 1
    var hi = ribbons.max
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (can(mid)) lo = mid
      else hi = mid - 1
    }
    if (can(lo)) lo else 0
  }
}
