// LeetCode 1976 - Number of Ways to Arrive at Destination
// https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/

import scala.collection.mutable

object Solution {
  def countPaths(n: Int, roads: Array[Array[Int]]): Int = {
    val MOD = 1000000007
    val g = Array.fill(n)(mutable.ArrayBuffer.empty[(Int, Int)])
    for (r <- roads) {
      g(r(0)) += ((r(1), r(2)))
      g(r(1)) += ((r(0), r(2)))
    }
    val dist = Array.fill(n)(Long.MaxValue / 4)
    val ways = Array.ofDim[Int](n)
    dist(0) = 0
    ways(0) = 1
    val pq = mutable.PriorityQueue.empty[(Long, Int)](Ordering.by[(Long, Int), Long](-_._1))
    pq.enqueue((0L, 0))
    while (pq.nonEmpty) {
      val (d, u) = pq.dequeue()
      if (d <= dist(u)) {
        for ((v, w) <- g(u)) {
          val nd = d + w
          if (nd < dist(v)) {
            dist(v) = nd
            ways(v) = ways(u)
            pq.enqueue((nd, v))
          } else if (nd == dist(v)) {
            ways(v) = (ways(v) + ways(u)) % MOD
          }
        }
      }
    }
    ways(n - 1)
  }
}
