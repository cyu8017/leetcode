// LeetCode 3047 - Find the Largest Area of Square Inside Two Rectangles
// https://leetcode.com/problems/find-the-largest-area-of-square-inside-two-rectangles/

object Solution {
  def largestSquareArea(bottomLeft: Array[Array[Int]], topRight: Array[Array[Int]]): Long = {
    var ans = 0L
    val n = bottomLeft.length
    var i = 0
    while (i < n) {
      val x1 = bottomLeft(i)(0)
      val y1 = bottomLeft(i)(1)
      val x2 = topRight(i)(0)
      val y2 = topRight(i)(1)
      var j = i + 1
      while (j < n) {
        val x3 = bottomLeft(j)(0)
        val y3 = bottomLeft(j)(1)
        val x4 = topRight(j)(0)
        val y4 = topRight(j)(1)
        val ww = math.min(x2, x4) - math.max(x1, x3)
        val h = math.min(y2, y4) - math.max(y1, y3)
        val e = math.min(ww, h)
        if (e > 0) ans = math.max(ans, e.toLong * e)
        j += 1
      }
      i += 1
    }
    ans
  }
}
