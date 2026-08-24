// LeetCode 3281 - Maximize Score of Numbers in Ranges
// https://leetcode.com/problems/maximize-score-of-numbers-in-ranges/

object Solution {
  def maxPossibleScore(start: Array[Int], d: Int): Int = {
    java.util.Arrays.sort(start)
    val n = start.length
    var lo = 0
    var hi = start(n - 1) + d - start(0) + 1
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (ok(start, d, mid)) lo = mid else hi = mid - 1
    }
    lo
  }

  def ok(start: Array[Int], d: Int, mid: Int): Boolean = {
    var prev = start(0).toLong
    var i = 1
    while (i < start.length) {
      val need = prev + mid
      val cur = start(i).toLong
      if (need > cur + d) return false
      prev = if (need > cur) need else cur
      i += 1
    }
    true
  }
}
