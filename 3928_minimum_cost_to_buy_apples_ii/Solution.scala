// LeetCode 3928 - Minimum Cost to Buy Apples II
// https://leetcode.com/problems/minimum-cost-to-buy-apples-ii/

import scala.collection.mutable

object Solution {
  private case class Edge(to: Int, empty: Int, full: Int)

  def minCostToBuyApples(n: Int, prices: Array[Int], roads: Array[Array[Int]]): Array[Long] = {
    val g = Array.fill(n)(mutable.ArrayBuffer.empty[Edge])
    for (road <- roads) {
      val empty = road(2)
      val full = road(2) * road(3)
      g(road(0)) += Edge(road(1), empty, full)
      g(road(1)) += Edge(road(0), empty, full)
    }
    val inf = 1L << 62
    val answer = new Array[Long](n)
    var source = 0
    while (source < n) {
      val emptyDist = dijkstra(n, g, source, carrying = false, inf)
      val fullDist = dijkstra(n, g, source, carrying = true, inf)
      var best = prices(source).toLong
      var shop = 0
      while (shop < n) {
        if (emptyDist(shop) != inf && fullDist(shop) != inf) {
          val total = emptyDist(shop) + fullDist(shop) + prices(shop)
          if (total < best) best = total
        }
        shop += 1
      }
      answer(source) = best
      source += 1
    }
    answer
  }

  private def dijkstra(
      n: Int,
      g: Array[mutable.ArrayBuffer[Edge]],
      source: Int,
      carrying: Boolean,
      inf: Long
  ): Array[Long] = {
    val dist = Array.fill(n)(inf)
    dist(source) = 0
    val pq = mutable.PriorityQueue.empty[(Long, Int)](Ordering.by[(Long, Int), Long](_._1).reverse)
    pq.enqueue((0L, source))
    while (pq.nonEmpty) {
      val (d, node) = pq.dequeue()
      if (d == dist(node)) {
        for (e <- g(node)) {
          val weight = if (carrying) e.full else e.empty
          val next = d + weight
          if (next < dist(e.to)) {
            dist(e.to) = next
            pq.enqueue((next, e.to))
          }
        }
      }
    }
    dist
  }
}
