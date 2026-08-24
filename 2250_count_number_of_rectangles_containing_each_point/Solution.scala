// LeetCode 2250 - Count Number of Rectangles Containing Each Point
// https://leetcode.com/problems/count-number-of-rectangles-containing-each-point/

object Solution {
  def countRectangles(rectangles: Array[Array[Int]], points: Array[Array[Int]]): Array[Int] = {
    val byH = Array.fill(101)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (r <- rectangles) byH(r(1)) += r(0)
    var h = 1
    while (h <= 100) {
      val sorted = byH(h).sorted
      byH(h).clear()
      byH(h) ++= sorted
      h += 1
    }
    val ans = new Array[Int](points.length)
    var i = 0
    while (i < points.length) {
      val x = points(i)(0)
      val y = points(i)(1)
      var cnt = 0
      h = y
      while (h <= 100) {
        val xs = byH(h)
        var lo = 0
        var hi = xs.length
        while (lo < hi) {
          val mid = (lo + hi) / 2
          if (xs(mid) < x) lo = mid + 1 else hi = mid
        }
        cnt += xs.length - lo
        h += 1
      }
      ans(i) = cnt
      i += 1
    }
    ans
  }
}
