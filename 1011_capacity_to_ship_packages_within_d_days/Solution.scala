// LeetCode 1011 - Capacity To Ship Packages Within D Days
// https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

object Solution {
  def shipWithinDays(weights: Array[Int], days: Int): Int = {
    var lo = weights.max
    var hi = weights.sum
    def can(cap: Int): Boolean = {
      var need = 1
      var cur = 0
      for (w <- weights) {
        if (cur + w > cap) {
          need += 1
          cur = 0
        }
        cur += w
      }
      need <= days
    }
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (can(mid)) hi = mid else lo = mid + 1
    }
    lo
  }
}
