// LeetCode 0539 - Minimum Time Difference
// https://leetcode.com/problems/minimum-time-difference/

object Solution {
  def findMinDifference(timePoints: List[String]): Int = {
    val minutes = timePoints.map { time =>
      val parts = time.split(":")
      parts(0).toInt * 60 + parts(1).toInt
    }.sorted

    var best = minutes.last - minutes.head
    for (i <- 1 until minutes.length) {
      best = math.min(best, minutes(i) - minutes(i - 1))
    }
    math.min(best, 24 * 60 - minutes.last + minutes.head)
  }
}
