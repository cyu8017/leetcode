// LeetCode 3009 - Maximum Number of Intersections on the Chart
// https://leetcode.com/problems/maximum-number-of-intersections-on-the-chart/

object Solution {
  def maxIntersectionCount(y: Array[Int]): Int = {
    val n = y.length
    val line = scala.collection.mutable.TreeMap[Int, Int]()
    var i = 1
    while (i < n) {
      val start = 2 * y(i - 1)
      var end = 2 * y(i)
      if (i != n - 1) {
        if (y(i) > y(i - 1)) end -= 1 else end += 1
      }
      var a = start
      var b = end
      if (a > b) { val t = a; a = b; b = t }
      line(a) = line.getOrElse(a, 0) + 1
      line(b + 1) = line.getOrElse(b + 1, 0) - 1
      i += 1
    }
    var ans = 0
    var cur = 0
    for (v <- line.values) {
      cur += v
      if (cur > ans) ans = cur
    }
    ans
  }
}
