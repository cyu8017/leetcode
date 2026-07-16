// LeetCode 0435 - Non-overlapping Intervals
// https://leetcode.com/problems/non-overlapping-intervals/

object Solution {
  def eraseOverlapIntervals(intervals: Array[Array[Int]]): Int = {
    val sorted = intervals.sortBy(_.apply(1))
    var removed = 0
    var end = Int.MinValue

    for (Array(start, finish) <- sorted) {
      if (start < end) {
        removed += 1
      } else {
        end = finish
      }
    }

    removed
  }
}
