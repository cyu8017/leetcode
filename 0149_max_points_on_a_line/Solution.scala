// LeetCode 0149 - Max Points on a Line
// https://leetcode.com/problems/max-points-on-a-line/

import scala.collection.mutable
object Solution {
  def maxPoints(points: Array[Array[Int]]): Int = {
    var best = 0
    for (i <- points.indices) {
      val slopes = mutable.Map[(Int, Int), Int]().withDefaultValue(0)
      var local = 1
      for (j <- i + 1 until points.length) {
        var dx = points(j)(0) - points(i)(0)
        var dy = points(j)(1) - points(i)(1)
        val divisor = gcd(dx, dy)
        dx /= divisor
        dy /= divisor
        if (dx < 0 || (dx == 0 && dy < 0)) { dx = -dx; dy = -dy }
        val key = (dx, dy)
        slopes(key) += 1
        local = Math.max(local, slopes(key) + 1)
      }
      best = Math.max(best, local)
    }
    best
  }
  private def gcd(first: Int, second: Int): Int = {
    var a = Math.abs(first)
    var b = Math.abs(second)
    while (b != 0) { val temp = a % b; a = b; b = temp }
    a
  }
}