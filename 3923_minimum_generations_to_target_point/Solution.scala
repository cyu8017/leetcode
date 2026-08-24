// LeetCode 3923 - Minimum Generations to Target Point
// https://leetcode.com/problems/minimum-generations-to-target-point/

import scala.collection.mutable

object Solution {
  case class P(a: Int, b: Int, c: Int)

  def minGenerations(points: Array[Array[Int]], target: Array[Int]): Int = {
    val targetPoint = P(target(0), target(1), target(2))
    val generation = mutable.HashMap.empty[P, Int]
    val all = mutable.ArrayBuffer.empty[P]
    for (values <- points) {
      val p = P(values(0), values(1), values(2))
      generation(p) = 0
      all += p
    }
    if (generation.contains(targetPoint)) return generation(targetPoint)
    var current = 1
    while (true) {
      val limit = all.size
      val added = mutable.ArrayBuffer.empty[P]
      var i = 0
      while (i < limit) {
        var j = i + 1
        while (j < limit) {
          if (!all(i).equals(all(j))) {
            val pi = all(i)
            val pj = all(j)
            val p = P((pi.a + pj.a) / 2, (pi.b + pj.b) / 2, (pi.c + pj.c) / 2)
            if (!generation.contains(p)) {
              generation(p) = current
              added += p
            }
          }
          j += 1
        }
        i += 1
      }
      if (generation.contains(targetPoint)) return generation(targetPoint)
      if (added.isEmpty) return -1
      all ++= added
      current += 1
    }
    -1
  }
}
