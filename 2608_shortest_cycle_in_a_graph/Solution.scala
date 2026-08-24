// LeetCode 2608 - Shortest Cycle in a Graph
// https://leetcode.com/problems/shortest-cycle-in-a-graph/

object Solution {
  def findShortestCycle(n: Int, edges: Array[Array[Int]]): Int = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    val INF = 1000000000
    var ans = INF
    var start = 0
    while (start < n) {
      val dist = Array.fill(n)(-1)
      val parent = Array.fill(n)(-1)
      val q = scala.collection.mutable.Queue.empty[Int]
      q.enqueue(start)
      dist(start) = 0
      while (q.nonEmpty) {
        val u = q.dequeue()
        g(u).foreach { v =>
          if (dist(v) < 0) {
            dist(v) = dist(u) + 1
            parent(v) = u
            q.enqueue(v)
          } else if (parent(u) != v) {
            val c = dist(u) + dist(v) + 1
            if (c < ans) ans = c
          }
        }
      }
      start += 1
    }
    if (ans == INF) -1 else ans
  }
}
