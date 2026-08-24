// LeetCode 3733 - Minimum Time To Complete All Deliveries
// https://leetcode.com/problems/minimum-time-to-complete-all-deliveries/

object Solution {
  def minimumTime(d: Array[Int], r: Array[Int]): Long = {
    var lo = 1L
    var hi = 8e18.toLong
    while (lo < hi) {
      val mid = lo + (hi - lo) / 2
      if (ok(mid, d, r)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def ok(T: Long, d: Array[Int], r: Array[Int]): Boolean = {
    val w0 = T - T / r(0)
    val w1 = T - T / r(1)
    w0 + w1 >= d(0).toLong + d(1)
  }
}
