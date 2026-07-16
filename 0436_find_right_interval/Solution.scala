// LeetCode 0436 - Find Right Interval
// https://leetcode.com/problems/find-right-interval/

object Solution {
  def findRightInterval(intervals: Array[Array[Int]]): Array[Int] = {
    val indexed = intervals.zipWithIndex.map { case (Array(start, _), index) => (start, index) }.sortBy(_._1)
    val starts = indexed.map(_._1)

    intervals.map { case Array(_, end) =>
      val position = lowerBound(starts, end)
      if (position == starts.length) -1 else indexed(position)._2
    }
  }

  private def lowerBound(values: Array[Int], target: Int): Int = {
    var left = 0
    var right = values.length
    while (left < right) {
      val mid = left + (right - left) / 2
      if (values(mid) < target) {
        left = mid + 1
      } else {
        right = mid
      }
    }
    left
  }
}
