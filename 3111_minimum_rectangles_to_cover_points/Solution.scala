// LeetCode 3111 - Minimum Rectangles to Cover Points
// https://leetcode.com/problems/minimum-rectangles-to-cover-points/

object Solution {
  def minRectanglesToCoverPoints(points: Array[Array[Int]], w: Int): Int = {
    val pts = points.sortBy(_(0))
    var ans = 0
    var x1 = -1
    pts.foreach { p =>
      if (p(0) > x1) {
        ans += 1
        x1 = p(0) + w
      }
    }
    ans
  }
}
