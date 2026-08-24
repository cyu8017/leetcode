// LeetCode 3924 - Minimum Threshold Path With Limited Heavy Edges
// https://leetcode.com/problems/minimum-threshold-path-with-limited-heavy-edges/

import scala.collection.mutable

object Solution {
  def minThreshold(n: Int, edges: Array[Array[Int]], source: Int, target: Int, k: Int): Int = {
    if (source == target) return 0
    val g = Array.fill(n)(mutable.ArrayBuffer.empty[(Int, Int)])
    var maxWeight = 0
    for (e <- edges) {
      g(e(0)) += ((e(1), e(2)))
      g(e(1)) += ((e(0), e(2)))
      maxWeight = math.max(maxWeight, e(2))
    }
    if (!can(n, g, source, target, k, maxWeight)) return -1
    var lo = 0
    var hi = maxWeight
    while (lo < hi) {
      val mid = lo + (hi - lo) / 2
      if (can(n, g, source, target, k, mid)) hi = mid
      else lo = mid + 1
    }
    lo
  }

  private def can(
      n: Int,
      g: Array[mutable.ArrayBuffer[(Int, Int)]],
      source: Int,
      target: Int,
      k: Int,
      threshold: Int
  ): Boolean = {
    val inf = 1000000000
    val dist = Array.fill(n)(inf)
    dist(source) = 0
    val dq = mutable.ArrayDeque[Int]()
    dq.append(source)
    while (dq.nonEmpty) {
      val u = dq.removeHead()
      for ((to, weight) <- g(u)) {
        val cost = if (weight > threshold) 1 else 0
        if (dist(u) + cost < dist(to) && dist(u) + cost <= k) {
          dist(to) = dist(u) + cost
          if (cost == 0) dq.prepend(to)
          else dq.append(to)
        }
      }
    }
    dist(target) <= k
  }
}
