// LeetCode 1266 - Minimum Time Visiting All Points
// https://leetcode.com/problems/minimum-time-visiting-all-points/

object Solution {
  def minTimeToVisitAllPoints(points: Array[Array[Int]]): Int =
    points.zip(points.tail).map { case (a, b) => math.max(math.abs(a(0) - b(0)), math.abs(a(1) - b(1))) }.sum
}
