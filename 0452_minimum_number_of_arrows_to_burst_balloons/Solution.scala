// LeetCode 0452 - Minimum Number of Arrows to Burst Balloons
// https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

object Solution {
  def findMinArrowShots(points: Array[Array[Int]]): Int = {
    if (points.isEmpty) return 0
    val sorted = points.sortBy(_.apply(1))
    var arrows = 1
    var end = sorted(0)(1)
    for (Array(start, finish) <- sorted.drop(1)) {
      if (start > end) {
        arrows += 1
        end = finish
      }
    }
    arrows
  }
}
