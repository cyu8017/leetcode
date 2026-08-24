// LeetCode 0973 - K Closest Points to Origin
// https://leetcode.com/problems/k-closest-points-to-origin/

object Solution {
  def kClosest(points: Array[Array[Int]], k: Int): Array[Array[Int]] = {
    points.sortBy(p => p(0).toLong * p(0) + p(1).toLong * p(1)).take(k)
  }
}
