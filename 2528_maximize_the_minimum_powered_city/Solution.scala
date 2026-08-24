// LeetCode 2528 - Maximize the Minimum Powered City
// https://leetcode.com/problems/maximize-the-minimum-powered-city/

object Solution {
  def maxPower(stations: Array[Int], r: Int, k: Int): Long = {
    val n = stations.length
    val diff = Array.fill(n + 1)(0L)
    var i = 0
    while (i < n) {
      val L = math.max(0, i - r)
      val R = math.min(n - 1, i + r)
      diff(L) += stations(i)
      diff(R + 1) -= stations(i)
      i += 1
    }
    val power = Array.fill(n)(0L)
    var cur = 0L
    i = 0
    while (i < n) {
      cur += diff(i)
      power(i) = cur
      i += 1
    }
    var lo = 0L
    var hi = k.toLong
    power.foreach { p => if (p > hi) hi = p }
    hi += k
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      if (ok(power, r, k.toLong, mid)) lo = mid
      else hi = mid - 1
    }
    lo
  }

  private def ok(power: Array[Long], r: Int, k: Long, x: Long): Boolean = {
    val n = power.length
    val extra = Array.fill(n + 1)(0L)
    var have = 0L
    var used = 0L
    var i = 0
    while (i < n) {
      have += extra(i)
      val need = x - (power(i) + have)
      if (need > 0) {
        used += need
        if (used > k) return false
        have += need
        val end = i + 2 * r
        if (end + 1 <= n) extra(end + 1) -= need
      }
      i += 1
    }
    true
  }
}
