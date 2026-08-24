// LeetCode 0963 - Minimum Area Rectangle II
// https://leetcode.com/problems/minimum-area-rectangle-ii/

object Solution {
  def minAreaFreeRect(points: Array[Array[Int]]): Double = {
    val n = points.length
    val groups = scala.collection.mutable.Map.empty[String, scala.collection.mutable.ArrayBuffer[Array[Int]]]
    var i = 0
    while (i < n) {
      var j = i + 1
      while (j < n) {
        val cx = points(i)(0).toLong + points(j)(0)
        val cy = points(i)(1).toLong + points(j)(1)
        val dx = points(i)(0).toLong - points(j)(0)
        val dy = points(i)(1).toLong - points(j)(1)
        val dist = dx * dx + dy * dy
        val key = cx + "#" + cy + "#" + dist
        groups.getOrElseUpdate(key, scala.collection.mutable.ArrayBuffer.empty[Array[Int]]) += Array(i, j)
        j += 1
      }
      i += 1
    }
    var ans = 1e300
    groups.values.foreach { pairs =>
      var a = 0
      while (a < pairs.length) {
        var b = a + 1
        while (b < pairs.length) {
          val p1 = pairs(a)(0)
          val p2 = pairs(b)(0)
          val q2 = pairs(b)(1)
          val d1 = math.hypot(points(p1)(0) - points(p2)(0), points(p1)(1) - points(p2)(1))
          val d2 = math.hypot(points(p1)(0) - points(q2)(0), points(p1)(1) - points(q2)(1))
          val area = d1 * d2
          if (area > 0) ans = math.min(ans, area)
          b += 1
        }
        a += 1
      }
    }
    if (ans >= 1e299) 0.0 else ans
  }
}
