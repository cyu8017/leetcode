// LeetCode 2642 - Design Graph With Shortest Path Calculator
// https://leetcode.com/problems/design-graph-with-shortest-path-calculator/

import scala.collection.mutable

class Graph(_n: Int, edges: Array[Array[Int]]) {
  private val g = Array.fill(_n)(mutable.ArrayBuffer.empty[Array[Int]])
  {
    var i = 0
    while (i < edges.length) {
      val e = edges(i)
      g(e(0)) += Array(e(1), e(2))
      i += 1
    }
  }

  def addEdge(edge: Array[Int]): Unit = {
    g(edge(0)) += Array(edge(1), edge(2))
  }

  def shortestPath(node1: Int, node2: Int): Int = {
    val n = g.length
    val dist = Array.fill(n)(1 << 30)
    dist(node1) = 0
    val pq = mutable.PriorityQueue.empty[(Int, Int)](Ordering.by[(Int, Int), Int](_._2).reverse)
    pq.enqueue((node1, 0))
    while (pq.nonEmpty) {
      val (u, d) = pq.dequeue()
      if (u == node2) return d
      if (d <= dist(u)) {
        g(u).foreach { e =>
          val nd = d + e(1)
          if (nd < dist(e(0))) {
            dist(e(0)) = nd
            pq.enqueue((e(0), nd))
          }
        }
      }
    }
    -1
  }
}
