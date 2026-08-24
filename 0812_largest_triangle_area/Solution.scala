// LeetCode 0812 - Largest Triangle Area
// https://leetcode.com/problems/largest-triangle-area/

object Solution {
  def largestTriangleArea(points: Array[Array[Int]]): Double = {
    var best = 0.0
    val n = points.length
    var i = 0
    while (i < n) {
      val x1 = points(i)(0); val y1 = points(i)(1)
      var j = i + 1
      while (j < n) {
        val x2 = points(j)(0); val y2 = points(j)(1)
        var k = j + 1
        while (k < n) {
          val x3 = points(k)(0); val y3 = points(k)(1)
          val area = math.abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0
          best = math.max(best, area)
          k += 1
        }
        j += 1
      }
      i += 1
    }
    best
  }
}
