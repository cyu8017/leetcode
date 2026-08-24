// LeetCode 3380 - Maximum Area Rectangle With Point Constraints I
// https://leetcode.com/problems/maximum-area-rectangle-with-point-constraints-i/

object Solution {
  private def pack(x: Int, y: Int): Long = (x.toLong << 32) ^ (y.toLong & 0xffffffffL)

  def maxRectangleArea(points: Array[Array[Int]]): Int = {
    val set = scala.collection.mutable.HashSet.empty[Long]
    for (p <- points) set += pack(p(0), p(1))
    var ans = -1
    val n = points.length
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        val x1 = points(i)(0)
        val y1 = points(i)(1)
        val x2 = points(j)(0)
        val y2 = points(j)(1)
        if (x1 != x2 && y1 != y2 && set.contains(pack(x1, y2)) && set.contains(pack(x2, y1))) {
          val minX = math.min(x1, x2)
          val maxX = math.max(x1, x2)
          val minY = math.min(y1, y2)
          val maxY = math.max(y1, y2)
          var ok = true
          for (p <- points if ok) {
            val x = p(0)
            val y = p(1)
            if (x > minX && x < maxX && y > minY && y < maxY) ok = false
            else {
              val onBorder = ((x == minX || x == maxX) && y >= minY && y <= maxY) ||
                ((y == minY || y == maxY) && x >= minX && x <= maxX)
              if (onBorder) {
                val isCorner = (x == minX || x == maxX) && (y == minY || y == maxY)
                if (!isCorner) ok = false
              }
            }
          }
          if (ok) {
            val area = (maxX - minX) * (maxY - minY)
            if (area > ans) ans = area
          }
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
