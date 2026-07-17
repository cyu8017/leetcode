// LeetCode 1732 - Find the Highest Altitude
// https://leetcode.com/problems/find-the-highest-altitude/

object Solution {
  def largestAltitude(gain: Array[Int]): Int = {
    var altitude = 0
    var best = 0
    gain.foreach { change =>
      altitude += change
      best = math.max(best, altitude)
    }
    best
  }
}
