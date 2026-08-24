// LeetCode 2473 - Minimum Cost to Buy Apples
// https://leetcode.com/problems/minimum-cost-to-buy-apples/

object Solution {
  def minCost(n: Int, roads: Array[Array[Int]], appleCost: Array[Int], k: Int): Array[Long] = {
    val g = Array.fill(n + 1)(scala.collection.mutable.ArrayBuffer.empty[(Int, Int)])
    roads.foreach { r =>
      g(r(0)) += ((r(1), r(2)))
      g(r(1)) += ((r(0), r(2)))
    }
    val ans = new Array[Long](n)
    val INF = 1L << 60
    implicit val ord: Ordering[(Long, Int)] = Ordering.by[(Long, Int), Long](_._1).reverse
    var start = 1
    while (start <= n) {
      val dist = Array.fill(n + 1)(INF)
      dist(start) = 0
      val pq = scala.collection.mutable.PriorityQueue.empty[(Long, Int)]
      pq.enqueue((0L, start))
      while (pq.nonEmpty) {
        val (d, u) = pq.dequeue()
        if (d == dist(u)) {
          g(u).foreach { case (v, w) =>
            val nd = d + w
            if (nd < dist(v)) {
              dist(v) = nd
              pq.enqueue((nd, v))
            }
          }
        }
      }
      var best = INF
      var city = 1
      while (city <= n) {
        val cost = dist(city) * (k + 1) + appleCost(city - 1)
        if (cost < best) best = cost
        city += 1
      }
      ans(start - 1) = best
      start += 1
    }
    ans
  }
}
