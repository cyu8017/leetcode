// LeetCode 3650 - Minimum Cost Path with Edge Reversals
// https://leetcode.com/problems/minimum-cost-path-with-edge-reversals/

object Solution {
  def minCost(n: Int, edges: Array[Array[Int]]): Int = {
    val g = Array.fill(n)(new java.util.ArrayList[Array[Int]]())
    for (e <- edges) {
      val u = e(0)
      val v = e(1)
      val w = e(2)
      g(u).add(Array(v, w))
      g(v).add(Array(u, w * 2))
    }
    val inf = Int.MaxValue / 2
    val dist = Array.fill(n)(inf)
    dist(0) = 0
    val pq = new java.util.PriorityQueue[Array[Int]]((a: Array[Int], b: Array[Int]) => Integer.compare(a(0), b(0)))
    pq.offer(Array(0, 0))
    while (!pq.isEmpty) {
      val cur = pq.poll()
      val d = cur(0)
      val u = cur(1)
      if (d <= dist(u)) {
        if (u == n - 1) return d
        val it = g(u).iterator()
        while (it.hasNext) {
          val e = it.next()
          val v = e(0)
          val w = e(1)
          val nd = d + w
          if (nd < dist(v)) {
            dist(v) = nd
            pq.offer(Array(nd, v))
          }
        }
      }
    }
    -1
  }
}
