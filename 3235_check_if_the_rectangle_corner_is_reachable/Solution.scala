// LeetCode 3235 - Check if the Rectangle Corner Is Reachable
// https://leetcode.com/problems/check-if-the-rectangle-corner-is-reachable/

object Solution {
  def canReachCorner(xCorner: Int, yCorner: Int, circles: Array[Array[Int]]): Boolean = {
    val n = circles.length
    val vis = new Array[Boolean](n)
    def inCircle(x: Int, y: Int, cx: Int, cy: Int, r: Int): Boolean = {
      val dx = (x - cx).toLong
      val dy = (y - cy).toLong
      dx * dx + dy * dy <= r.toLong * r
    }
    def crossLeftTop(cx: Int, cy: Int, r: Int): Boolean = {
      val a = math.abs(cx) <= r && cy >= 0 && cy <= yCorner
      val b = math.abs(cy - yCorner) <= r && cx >= 0 && cx <= xCorner
      a || b
    }
    def crossRightBottom(cx: Int, cy: Int, r: Int): Boolean = {
      val a = math.abs(cx - xCorner) <= r && cy >= 0 && cy <= yCorner
      val b = math.abs(cy) <= r && cx >= 0 && cx <= xCorner
      a || b
    }
    def dfs(i: Int): Boolean = {
      val x1 = circles(i)(0)
      val y1 = circles(i)(1)
      val r1 = circles(i)(2)
      if (crossRightBottom(x1, y1, r1)) return true
      vis(i) = true
      var j = 0
      while (j < n) {
        if (!vis(j)) {
          val x2 = circles(j)(0)
          val y2 = circles(j)(1)
          val r2 = circles(j)(2)
          if ((x1 - x2).toLong * (x1 - x2) + (y1 - y2).toLong * (y1 - y2) <= (r1 + r2).toLong * (r1 + r2)) {
            if (x1.toLong * r2 + x2.toLong * r1 < (r1 + r2).toLong * xCorner
                && y1.toLong * r2 + y2.toLong * r1 < (r1 + r2).toLong * yCorner
                && dfs(j)) return true
          }
        }
        j += 1
      }
      false
    }
    var i = 0
    while (i < n) {
      val x = circles(i)(0)
      val y = circles(i)(1)
      val r = circles(i)(2)
      if (inCircle(0, 0, x, y, r) || inCircle(xCorner, yCorner, x, y, r)) return false
      if (!vis(i) && crossLeftTop(x, y, r) && dfs(i)) return false
      i += 1
    }
    true
  }
}
