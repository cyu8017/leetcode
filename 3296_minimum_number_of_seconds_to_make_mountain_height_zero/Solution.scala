// LeetCode 3296 - Minimum Number of Seconds to Make Mountain Height Zero
// https://leetcode.com/problems/minimum-number-of-seconds-to-make-mountain-height-zero/

object Solution {
  def minNumberOfSeconds(mountainHeight: Int, workerTimes: Array[Int]): Long = {
    var lo = 0L
    var hi = 1000000000000000000L
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (ok(mid, mountainHeight, workerTimes)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def ok(t: Long, mountainHeight: Int, workerTimes: Array[Int]): Boolean = {
    var total = 0L
    for (w <- workerTimes) {
      var l = 0L
      var h = mountainHeight.toLong
      while (l < h) {
        val mid = (l + h + 1) / 2
        if (w.toLong * mid * (mid + 1) / 2 <= t) l = mid
        else h = mid - 1
      }
      total += l
      if (total >= mountainHeight) return true
    }
    total >= mountainHeight
  }
}
