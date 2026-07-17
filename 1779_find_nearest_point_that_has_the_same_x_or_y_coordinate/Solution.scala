// LeetCode 1779 - Find Nearest Point That Has the Same X or Y Coordinate
// https://leetcode.com/problems/find-nearest-point-that-has-the-same-x-or-y-coordinate/

object Solution {
  def nearestValidPoint(x: Int, y: Int, points: Array[Array[Int]]): Int = {
    var best = Int.MaxValue
    var ans = -1
    for (i <- points.indices) {
      val px = points(i)(0)
      val py = points(i)(1)
      if (px == x || py == y) {
        val dist = math.abs(px - x) + math.abs(py - y)
        if (dist < best) {
          best = dist
          ans = i
        }
      }
    }
    ans
  }
}
