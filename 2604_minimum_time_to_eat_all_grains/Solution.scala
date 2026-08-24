// LeetCode 2604 - Minimum Time to Eat All Grains
// https://leetcode.com/problems/minimum-time-to-eat-all-grains/

object Solution {
  def minimumTime(hens: Array[Int], grains: Array[Int]): Int = {
    java.util.Arrays.sort(hens)
    java.util.Arrays.sort(grains)
    var lo = 0
    var hi = 2000000000
    while (lo < hi) {
      val mid = lo + (hi - lo) / 2
      if (ok(hens, grains, mid)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def ok(hens: Array[Int], grains: Array[Int], t: Int): Boolean = {
    var j = 0
    hens.foreach { h =>
      if (j >= grains.length) return true
      if (grains(j) >= h) {
        while (j < grains.length && grains(j) - h <= t) j += 1
      } else {
        if (h - grains(j) > t) return false
        val left = h - grains(j)
        val maxRight1 = t - 2 * left
        val maxRight2 = (t - left) / 2
        var reach = h
        if (maxRight1 > maxRight2) {
          if (maxRight1 > 0) reach = h + maxRight1
        } else {
          if (maxRight2 > 0) reach = h + maxRight2
        }
        while (j < grains.length && grains(j) <= reach) j += 1
      }
    }
    j >= grains.length
  }
}
