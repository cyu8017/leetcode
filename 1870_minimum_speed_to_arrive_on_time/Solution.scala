// LeetCode 1870 - Minimum Speed to Arrive on Time
// https://leetcode.com/problems/minimum-speed-to-arrive-on-time/

object Solution {
  def minSpeedOnTime(dist: Array[Int], hour: Double): Int = {
    val n = dist.length
    if (n - 1 >= hour) return -1

    def canArrive(speed: Int): Boolean = {
      var time = 0.0
      for (i <- 0 until n - 1) {
        time += (dist(i) + speed - 1) / speed
      }
      time += dist(n - 1).toDouble / speed
      time <= hour
    }

    if (!canArrive(10000000)) return -1
    var lo = 1
    var hi = 10000000
    while (lo < hi) {
      val mid = (lo + hi) / 2
      if (canArrive(mid)) hi = mid
      else lo = mid + 1
    }
    lo
  }
}
