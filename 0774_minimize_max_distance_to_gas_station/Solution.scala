// LeetCode 0774 - Minimize Max Distance to Gas Station
// https://leetcode.com/problems/minimize-max-distance-to-gas-station/

object Solution {
  def minmaxGasDist(stations: Array[Int], k: Int): Double = {
    def can(dist: Double): Boolean = {
      var needed = 0
      var i = 1
      while (i < stations.length) {
        needed += ((stations(i) - stations(i - 1)) / dist).toInt
        i += 1
      }
      needed <= k
    }
    var lo = 0.0
    var hi = (stations(stations.length - 1) - stations(0)).toDouble
    while (hi - lo > 1e-6) {
      val mid = (lo + hi) / 2.0
      if (can(mid)) hi = mid
      else lo = mid
    }
    hi
  }
}
