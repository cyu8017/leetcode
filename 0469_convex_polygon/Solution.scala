// LeetCode 0469 - Convex Polygon
// https://leetcode.com/problems/convex-polygon/

object Solution {
  def isConvex(points: Array[Array[Int]]): Boolean = {
    var direction = 0
    val count = points.length

    var index = 0
    while (index < count) {
      val x1 = points((index + 1) % count)(0) - points(index)(0)
      val y1 = points((index + 1) % count)(1) - points(index)(1)
      val x2 = points((index + 2) % count)(0) - points((index + 1) % count)(0)
      val y2 = points((index + 2) % count)(1) - points((index + 1) % count)(1)
      val cross = x1 * y2 - y1 * x2
      if (cross != 0) {
        val current = if (cross > 0) 1 else -1
        if (direction != 0 && direction != current) {
          return false
        }
        if (direction == 0) {
          direction = current
        }
      }
      index += 1
    }

    true
  }
}
