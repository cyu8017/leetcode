// LeetCode 2699 - Modify Graph Edge Weights
// https://leetcode.com/problems/modify-graph-edge-weights/

import scala.collection.mutable

object Solution {
  private val INF = 2000000000

  def modifiedGraphEdges(
    n: Int,
    edges: Array[Array[Int]],
    source: Int,
    destination: Int,
    target: Int
  ): Array[Array[Int]] = {
    var d = dijkstra(n, edges, source, ignoreNeg = true)
    if (d(destination) < target) return Array.empty[Array[Int]]
    var matched = d(destination) == target
    var i = 0
    while (i < edges.length) {
      if (edges(i)(2) == -1) {
        if (matched) {
          edges(i)(2) = INF
        } else {
          edges(i)(2) = 1
          d = dijkstra(n, edges, source, ignoreNeg = false)
          if (d(destination) <= target) {
            edges(i)(2) += target - d(destination)
            matched = true
          }
        }
      }
      i += 1
    }
    d = dijkstra(n, edges, source, ignoreNeg = false)
    if (d(destination) != target) Array.empty[Array[Int]] else edges
  }

  private def dijkstra(n: Int, edges: Array[Array[Int]], source: Int, ignoreNeg: Boolean): Array[Int] = {
    val dist = Array.fill(n)(INF)
    dist(source) = 0
    val pq = mutable.PriorityQueue.empty[(Int, Int)](Ordering.by[(Int, Int), Int](_._2).reverse)
    pq.enqueue((source, 0))
    while (pq.nonEmpty) {
      val (u, d) = pq.dequeue()
      if (d == dist(u)) {
        var i = 0
        while (i < edges.length) {
          val e = edges(i)
          val a = e(0)
          val b = e(1)
          var w = e(2)
          if (a == u || b == u) {
            val to = if (a == u) b else a
            var skip = false
            if (w == -1) {
              if (ignoreNeg) skip = true
              else w = 1
            }
            if (!skip && d + w < dist(to)) {
              dist(to) = d + w
              pq.enqueue((to, dist(to)))
            }
          }
          i += 1
        }
      }
    }
    dist
  }
}
