// LeetCode 1964 - Find the Longest Valid Obstacle Course at Each Position
// https://leetcode.com/problems/find-the-longest-valid-obstacle-course-at-each-position/

object Solution {
  def longestObstacleCourseAtEachPosition(obstacles: Array[Int]): Array[Int] = {
    val tails = scala.collection.mutable.ArrayBuffer.empty[Int]
    val ans = Array.ofDim[Int](obstacles.length)
    for (idx <- obstacles.indices) {
      val x = obstacles(idx)
      var lo = 0
      var hi = tails.length
      while (lo < hi) {
        val mid = (lo + hi) / 2
        if (tails(mid) <= x) lo = mid + 1
        else hi = mid
      }
      if (lo == tails.length) tails += x
      else tails(lo) = x
      ans(idx) = lo + 1
    }
    ans
  }
}
