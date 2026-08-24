// LeetCode 3123 - Find Edges in Shortest Paths
// https://leetcode.com/problems/find-edges-in-shortest-paths/

object Solution {
  def findAnswer(n: Int, edges: Array[Array[Int]]): Array[Boolean] = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Array[Int]])
    var i = 0
    while (i < edges.length) {
      val a = edges(i)(0)
      val b = edges(i)(1)
      val w = edges(i)(2)
      g(a) += Array(b, w, i)
      g(b) += Array(a, w, i)
      i += 1
    }
    val INF = 1 << 30
    val dist = Array.fill(n)(INF)
    dist(0) = 0
    val pq = new java.util.PriorityQueue[Array[Int]]((a: Array[Int], b: Array[Int]) => a(0) - b(0))
    pq.offer(Array(0, 0))
    while (!pq.isEmpty) {
      val cur = pq.poll()
      val da = cur(0)
      val a = cur(1)
      if (da <= dist(a)) {
        g(a).foreach { e =>
          val b = e(0)
          val w = e(1)
          if (dist(b) > dist(a) + w) {
            dist(b) = dist(a) + w
            pq.offer(Array(dist(b), b))
          }
        }
      }
    }
    val ans = new Array[Boolean](edges.length)
    if (dist(n - 1) == INF) return ans
    val q = new java.util.ArrayDeque[Integer]()
    q.offer(n - 1)
    while (!q.isEmpty) {
      val a = q.poll()
      g(a).foreach { e =>
        val b = e(0)
        val w = e(1)
        val ei = e(2)
        if (dist(a) == dist(b) + w) {
          ans(ei) = true
          q.offer(b)
        }
      }
    }
    ans
  }
}
