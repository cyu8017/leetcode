// LeetCode 1610 - Maximum Number of Visible Points
// https://leetcode.com/problems/maximum-number-of-visible-points/

object Solution {
  def visiblePoints(points: Array[Array[Int]], angle: Int, location: Array[Int]): Int = {
    var same = 0
    val a = scala.collection.mutable.ArrayBuffer.empty[Double]
    for (p <- points) {
      val dx = p(0) - location(0)
      val dy = p(1) - location(1)
      if (dx == 0 && dy == 0) same += 1
      else a += math.atan2(dy, dx)
    }
    val sorted = a.sorted
    val ext = sorted ++ sorted.map(_ + 2 * math.Pi)
    val width = math.toRadians(angle) + 1e-12
    var left = 0
    var best = 0
    ext.indices.foreach { right =>
      while (ext(right) - ext(left) > width) left += 1
      best = math.max(best, math.min(sorted.length, right - left + 1))
    }
    best + same
  }
}
