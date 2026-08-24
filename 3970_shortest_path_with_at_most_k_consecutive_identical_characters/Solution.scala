// LeetCode 3970 - Shortest Path With at Most K Consecutive Identical Characters
// https://leetcode.com/problems/shortest-path-with-at-most-k-consecutive-identical-characters/

import scala.collection.mutable

object Solution {
  def shortestPath(n: Int, edges: Array[Array[Int]], labels: String, k: Int): Long = {
    val graph = Array.fill(n)(mutable.ArrayBuffer.empty[(Int, Int)])
    for (edge <- edges) graph(edge(0)) += ((edge(1), edge(2)))
    val infinity = Long.MaxValue / 4
    val distances = Array.fill(n, k + 1)(infinity)
    distances(0)(1) = 0
    val pq = mutable.PriorityQueue.empty[(Long, Int, Int)](Ordering.by[(Long, Int, Int), Long](_._1).reverse)
    pq.enqueue((0L, 0, 1))
    while (pq.nonEmpty) {
      val (distance, node, run) = pq.dequeue()
      if (distance == distances(node)(run)) {
        if (node == n - 1) return distance
        for ((to, weight) <- graph(node)) {
          var nextRun = 1
          if (labels.charAt(node) == labels.charAt(to)) nextRun = run + 1
          if (nextRun <= k) {
            val nextDistance = distance + weight
            if (nextDistance < distances(to)(nextRun)) {
              distances(to)(nextRun) = nextDistance
              pq.enqueue((nextDistance, to, nextRun))
            }
          }
        }
      }
    }
    -1
  }
}
