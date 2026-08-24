// LeetCode 2093 - Minimum Cost to Reach City With Discounts
// https://leetcode.com/problems/minimum-cost-to-reach-city-with-discounts/

object Solution {
  def minimumCost(n: Int, highways: Array[Array[Int]], discounts: Int): Int = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[(Int, Int)])
    highways.foreach { h =>
      g(h(0)) += ((h(1), h(2)))
      g(h(1)) += ((h(0), h(2)))
    }
    val Inf = 1 << 30
    val dist = Array.fill(n, discounts + 1)(Inf)
    val pq = scala.collection.mutable.PriorityQueue.empty[(Int, Int, Int)](Ordering.by[(Int, Int, Int), Int](_._1).reverse)
    dist(0)(discounts) = 0
    pq.enqueue((0, 0, discounts))
    while (pq.nonEmpty) {
      val (cost, city, disc) = pq.dequeue()
      if (city == n - 1) return cost
      if (cost <= dist(city)(disc)) {
        g(city).foreach { case (v, w) =>
          if (cost + w < dist(v)(disc)) {
            dist(v)(disc) = cost + w
            pq.enqueue((dist(v)(disc), v, disc))
          }
          if (disc > 0 && cost + w / 2 < dist(v)(disc - 1)) {
            dist(v)(disc - 1) = cost + w / 2
            pq.enqueue((dist(v)(disc - 1), v, disc - 1))
          }
        }
      }
    }
    -1
  }
}
