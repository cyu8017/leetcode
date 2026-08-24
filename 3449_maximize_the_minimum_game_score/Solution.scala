// LeetCode 3449 - Maximize the Minimum Game Score
// https://leetcode.com/problems/maximize-the-minimum-game-score/

object Solution {
  def maxScore(points: Array[Int], m: Int): Long = {
    var lo = 0L
    var hi = 1e18.toLong
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (ok(points, m, mid)) lo = mid
      else hi = mid - 1
    }
    lo
  }

  private def ok(points: Array[Int], m: Int, mid: Long): Boolean = {
    var need = 0L
    var extra = 0L
    points.foreach { p =>
      val req = (mid + p - 1) / p
      if (req > extra) {
        val visits = req - extra
        need += 2 * visits - 1
        extra = visits - 1
      } else {
        need += 1
        extra = 0
      }
      if (need > m) return false
    }
    need <= m
  }
}
