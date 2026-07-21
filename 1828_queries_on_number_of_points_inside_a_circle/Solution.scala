// LeetCode 1828 - Queries on Number of Points Inside a Circle
// https://leetcode.com/problems/queries-on-number-of-points-inside-a-circle/

object Solution {
  def countPoints(points: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    queries.map { q =>
      val xq = q(0); val yq = q(1); val r = q(2)
      val r2 = r * r
      points.count { p =>
        val dx = p(0) - xq
        val dy = p(1) - yq
        dx * dx + dy * dy <= r2
      }
    }
  }
}
