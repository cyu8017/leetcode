// LeetCode 3625 - Count Number of Trapezoids II
// https://leetcode.com/problems/count-number-of-trapezoids-ii/

object Solution {
  def countTrapezoids(points: Array[Array[Int]]): Int = {
    val n = points.length
    val cnt1 = new java.util.HashMap[java.lang.Double, java.util.Map[java.lang.Double, Integer]]()
    val cnt2 = new java.util.HashMap[Integer, java.util.Map[java.lang.Double, Integer]]()
    var i = 0
    while (i < n) {
      val x1 = points(i)(0)
      val y1 = points(i)(1)
      var j = 0
      while (j < i) {
        val x2 = points(j)(0)
        val y2 = points(j)(1)
        val dx = x2 - x1
        val dy = y2 - y1
        val k: Double = if (dx == 0) 1e9 else dy.toDouble / dx
        val b: Double = if (dx == 0) x1.toDouble else (y1.toLong * dx - x1.toLong * dy).toDouble / dx
        cnt1.computeIfAbsent(k, (_: java.lang.Double) => new java.util.HashMap[java.lang.Double, Integer]()).merge(b, 1, Integer.sum)
        val p = (x1 + x2 + 2000) * 4000 + (y1 + y2 + 2000)
        cnt2.computeIfAbsent(p, (_: Integer) => new java.util.HashMap[java.lang.Double, Integer]()).merge(k, 1, Integer.sum)
        j += 1
      }
      i += 1
    }
    var ans = 0
    val it1 = cnt1.values().iterator()
    while (it1.hasNext) {
      val e = it1.next()
      var s = 0
      val it = e.values().iterator()
      while (it.hasNext) {
        val t = it.next().intValue()
        ans += s * t
        s += t
      }
    }
    val it2 = cnt2.values().iterator()
    while (it2.hasNext) {
      val e = it2.next()
      var s = 0
      val it = e.values().iterator()
      while (it.hasNext) {
        val t = it.next().intValue()
        ans -= s * t
        s += t
      }
    }
    ans
  }
}
