// LeetCode 2714 - Find Shortest Path With K Hops
// https://leetcode.com/problems/find-shortest-path-with-k-hops/

import scala.collection.mutable

object Solution {
  def shortestPathWithHops(n: Int, edges: Array[Array[Int]], s: Int, d: Int, k: Int): Int = {
    val g = Array.fill(n)(mutable.ArrayBuffer.empty[Array[Int]])
    var i = 0
    while (i < edges.length) {
      val e = edges(i)
      g(e(0)) += Array(e(1), e(2))
      g(e(1)) += Array(e(0), e(2))
      i += 1
    }
    val dist = Array.fill(n, k + 1)(Int.MaxValue / 4)
    dist(s)(0) = 0
    val pq = mutable.PriorityQueue.empty[(Int, Int, Int)](Ordering.by[(Int, Int, Int), Int](_._3).reverse)
    pq.enqueue((s, 0, 0))
    while (pq.nonEmpty) {
      val (u, hops, cd) = pq.dequeue()
      if (u == d) return cd
      if (cd <= dist(u)(hops)) {
        g(u).foreach { e =>
          val to = e(0)
          val w = e(1)
          if (cd + w < dist(to)(hops)) {
            dist(to)(hops) = cd + w
            pq.enqueue((to, hops, dist(to)(hops)))
          }
          if (hops < k && cd < dist(to)(hops + 1)) {
            dist(to)(hops + 1) = cd
            pq.enqueue((to, hops + 1, cd))
          }
        }
      }
    }
    -1
  }
}
