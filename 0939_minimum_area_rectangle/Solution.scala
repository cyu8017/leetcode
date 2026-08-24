// LeetCode 0939 - Minimum Area Rectangle
// https://leetcode.com/problems/minimum-area-rectangle/

object Solution {
  def minAreaRect(points: Array[Array[Int]]): Int = {
    val byX = scala.collection.mutable.TreeMap.empty[Int, scala.collection.mutable.ArrayBuffer[Int]]
    points.foreach { p =>
      byX.getOrElseUpdate(p(0), scala.collection.mutable.ArrayBuffer.empty[Int]) += p(1)
    }
    val last = scala.collection.mutable.Map.empty[String, Int]
    var ans = Long.MaxValue
    byX.foreach { case (x, ysBuf) =>
      val ys = ysBuf.sorted
      var i = 0
      while (i < ys.length) {
        var j = i + 1
        while (j < ys.length) {
          val key = ys(i) + "#" + ys(j)
          if (last.contains(key)) {
            ans = math.min(ans, math.abs(x.toLong - last(key)) * (ys(j) - ys(i)))
          }
          last(key) = x
          j += 1
        }
        i += 1
      }
    }
    if (ans == Long.MaxValue) 0 else ans.toInt
  }
}
