// LeetCode 1637 - Widest Vertical Area Between Two Points Containing No Points
// https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points/

object Solution {
  def maxWidthOfVerticalArea(points: Array[Array[Int]]): Int = {
    val xs = points.map(_(0)).sorted
    xs.indices.drop(1).map(i => xs(i) - xs(i - 1)).max
  }
}
