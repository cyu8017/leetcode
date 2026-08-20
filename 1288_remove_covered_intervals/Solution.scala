// LeetCode 1288 - Remove Covered Intervals
// https://leetcode.com/problems/remove-covered-intervals/

object Solution {
  def removeCoveredIntervals(intervals: Array[Array[Int]]): Int = {
    val sorted = intervals.sortBy(iv => (iv(0), -iv(1)))
    var answer = 0
    var farthest = -1
    for (iv <- sorted) {
      if (iv(1) > farthest) {
        answer += 1
        farthest = iv(1)
      }
    }
    answer
  }
}
