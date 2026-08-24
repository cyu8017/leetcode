// LeetCode 2188 - Minimum Time to Finish the Race
// https://leetcode.com/problems/minimum-time-to-finish-the-race/

object Solution {
  def minimumFinishTime(tires: Array[Array[Int]], changeTime: Int, numLaps: Int): Int = {
    val minTime = Array.fill(20)(1 << 30)
    tires.foreach { tire =>
      val f = tire(0)
      val r = tire(1)
      var t = f.toLong
      var lap = f.toLong
      var x = 1
      var stop = false
      while (x < 20 && t < minTime(x) && !stop) {
        minTime(x) = t.toInt
        lap *= r
        if (lap > changeTime + f) stop = true
        else {
          t += lap
          x += 1
        }
      }
    }
    val dp = Array.fill(numLaps + 1)(1 << 30)
    dp(0) = -changeTime
    var i = 1
    while (i <= numLaps) {
      var j = 1
      while (j <= i && j < 20) {
        dp(i) = math.min(dp(i), dp(i - j) + changeTime + minTime(j))
        j += 1
      }
      i += 1
    }
    dp(numLaps)
  }
}
