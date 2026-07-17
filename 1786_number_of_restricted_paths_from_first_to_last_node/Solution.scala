// LeetCode 1786 - Number of Restricted Paths From First to Last Node
// https://leetcode.com/problems/number-of-restricted-paths-from-first-to-last-node/

import scala.collection.mutable

object Solution {
  def countRestrictedPaths(n: Int, edges: Array[Array[Int]]): Int = {
    val adj = Array.fill(n + 1)(mutable.ArrayBuffer.empty[(Int, Int)])
    for (e <- edges) {
      adj(e(0)) += ((e(1), e(2)))
      adj(e(1)) += ((e(0), e(2)))
    }
    val dist = Array.fill(n + 1)(Long.MaxValue)
    dist(n) = 0L
    val heap = mutable.PriorityQueue.empty[(Long, Int)](Ordering.by[(Long, Int), Long](_._1).reverse)
    heap.enqueue((0L, n))
    while (heap.nonEmpty) {
      val (d, u) = heap.dequeue()
      if (d == dist(u)) {
        for ((v, w) <- adj(u)) {
          val nd = d + w
          if (nd < dist(v)) {
            dist(v) = nd
            heap.enqueue((nd, v))
          }
        }
      }
    }
    val order = (1 to n).sortBy(dist(_))
    val mod = 1000000007L
    val cnt = Array.fill(n + 1)(0L)
    cnt(n) = 1L
    for (u <- order if u != n) {
      for ((v, _) <- adj(u)) {
        if (dist(u) > dist(v)) {
          cnt(u) = (cnt(u) + cnt(v)) % mod
        }
      }
    }
    cnt(1).toInt
  }
}
