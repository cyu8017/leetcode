// LeetCode 1840 - Maximum Building Height
// https://leetcode.com/problems/maximum-building-height/

object Solution {
  def maxBuilding(n: Int, restrictions: Array[Array[Int]]): Int = {
    val points = scala.collection.mutable.ArrayBuffer((1, 0))
    points ++= restrictions.map(r => (r(0), r(1))).sortBy(_._1)
    if (points.last._1 != n) points += ((n, n - 1))

    for (i <- 1 until points.length) {
      val (prevId, prevH) = points(i - 1)
      val (currId, currH) = points(i)
      points(i) = (currId, math.min(currH, prevH + currId - prevId))
    }
    for (i <- points.length - 2 to 0 by -1) {
      val (nextId, nextH) = points(i + 1)
      val (currId, currH) = points(i)
      points(i) = (currId, math.min(currH, nextH + nextId - currId))
    }

    var best = points.map(_._2).max
    for (i <- 0 until points.length - 1) {
      val (id1, h1) = points(i)
      val (id2, h2) = points(i + 1)
      best = math.max(best, (h1 + h2 + id2 - id1) / 2)
    }
    best
  }
}
