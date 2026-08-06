// LeetCode 1928 - Minimum Cost to Reach Destination in Time
// https://leetcode.com/problems/minimum-cost-to-reach-destination-in-time/

import scala.collection.mutable

object Solution {
  def minCost(maxTime: Int, edges: Array[Array[Int]], passingFee: Array[Int]): Int = {
    val n = passingFee.length
    val graph = Array.fill(n)(mutable.ArrayBuffer.empty[(Int, Int)])
    for (e <- edges) {
      graph(e(0)) += ((e(1), e(2)))
      graph(e(1)) += ((e(0), e(2)))
    }
    val minTime = Array.fill(n)(maxTime + 1)
    val pq = mutable.PriorityQueue.empty[(Int, Int, Int)](Ordering.by[(Int, Int, Int), Int](-_._1))
    pq.enqueue((passingFee(0), 0, 0))
    while (pq.nonEmpty) {
      val (cost, time, u) = pq.dequeue()
      if (time < minTime(u)) {
        minTime(u) = time
        if (u == n - 1) return cost
        for ((v, dt) <- graph(u)) {
          val nt = time + dt
          if (nt <= maxTime && nt < minTime(v)) {
            pq.enqueue((cost + passingFee(v), nt, v))
          }
        }
      }
    }
    -1
  }
}
