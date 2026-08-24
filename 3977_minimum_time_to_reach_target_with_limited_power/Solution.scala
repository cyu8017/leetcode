// LeetCode 3977 - Minimum Time to Reach Target With Limited Power
// https://leetcode.com/problems/minimum-time-to-reach-target-with-limited-power/

import scala.collection.mutable

object Solution {
  def minTimeMaxPower(n: Int, edges: Array[Array[Int]], power: Int, cost: Array[Int], source: Int, target: Int): Array[Long] = {
    val INF = 1L << 62
    val g = Array.fill(n)(mutable.ArrayBuffer.empty[(Int, Int)])
    for (e <- edges) g(e(0)) += ((e(1), e(2)))
    val dist = Array.fill(n, power + 1)(INF)
    implicit val ord: Ordering[(Long, Long, Long)] =
      Ordering.Tuple3(Ordering.Long, Ordering.Long, Ordering.Long).reverse
    val pq = mutable.PriorityQueue.empty[(Long, Long, Long)]
    pq.enqueue((0L, -power.toLong, source.toLong))
    dist(source)(power) = 0
    while (pq.nonEmpty) {
      val (d, negP, uL) = pq.dequeue()
      var p = (-negP).toInt
      val u = uL.toInt
      if (u == target) return Array(d, p.toLong)
      if (d <= dist(u)(p) && p >= cost(u)) {
        p -= cost(u)
        for ((v, t) <- g(u)) {
          val nd = d + t
          if (nd < dist(v)(p)) {
            dist(v)(p) = nd
            pq.enqueue((nd, -p.toLong, v.toLong))
          }
        }
      }
    }
    Array(-1L, -1L)
  }
}
