// LeetCode 2141 - Maximum Running Time of N Computers
// https://leetcode.com/problems/maximum-running-time-of-n-computers/

object Solution {
  def maxRunTime(n: Int, batteries: Array[Int]): Long = {
    var sum = 0L
    batteries.foreach(b => sum += b)
    var lo = 1L
    var hi = sum / n
    while (lo < hi) {
      val mid = (lo + hi + 1) / 2
      var need = 0L
      batteries.foreach(b => need += math.min(b.toLong, mid))
      if (need >= mid * n) lo = mid
      else hi = mid - 1
    }
    lo
  }
}
