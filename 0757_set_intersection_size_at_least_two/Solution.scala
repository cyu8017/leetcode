// LeetCode 0757 - Set Intersection Size At Least Two
// https://leetcode.com/problems/set-intersection-size-at-least-two/

object Solution {
  def intersectionSizeTwo(intervals: Array[Array[Int]]): Int = {
    val arr = intervals.sortWith((a, b) => if (a(1) != b(1)) a(1) < b(1) else a(0) < b(0))
    var size = 0
    var first = -1
    var second = -1
    for (interval <- arr) {
      val left = interval(0)
      val right = interval(1)
      if (left > first) {
        if (left <= second) {
          size += 1
          first = second
          second = right
        } else {
          size += 2
          first = right - 1
          second = right
        }
      }
    }
    size
  }
}
