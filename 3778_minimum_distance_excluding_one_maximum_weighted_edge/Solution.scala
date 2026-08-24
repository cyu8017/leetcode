// LeetCode 3778 - Minimum Distance Excluding One Maximum Weighted Edge
// https://leetcode.com/problems/minimum-distance-excluding-one-maximum-weighted-edge/

object Solution {
  def minCostExcludingMax(n: Int, edges: Array[Array[Int]]): Long = {
    val g = Array.fill(n)(new java.util.ArrayList[Array[Int]]())
    edges.foreach { e =>
      val u = e(0); val v = e(1); val w = e(2)
      g(u).add(Array(v, w))
      g(v).add(Array(u, w))
    }
    val INF = 4e18.toLong
    val dist = Array.fill(n, 2)(INF)
    dist(0)(0) = 0
    val pq = new java.util.PriorityQueue[Array[Long]]((a: Array[Long], b: Array[Long]) => java.lang.Long.compare(a(0), b(0)))
    pq.offer(Array(0L, 0L, 0L))
    while (!pq.isEmpty) {
      val cur = pq.poll()
      val c = cur(0)
      val u = cur(1).toInt
      val used = cur(2).toInt
      if (c <= dist(u)(used)) {
        if (u == n - 1 && used == 1) return c
        val it = g(u).iterator()
        while (it.hasNext) {
          val e = it.next()
          val v = e(0)
          val w = e(1)
          var nxt = c + w
          if (nxt < dist(v)(used)) {
            dist(v)(used) = nxt
            pq.offer(Array(nxt, v.toLong, used.toLong))
          }
          if (used == 0) {
            nxt = c
            if (nxt < dist(v)(1)) {
              dist(v)(1) = nxt
              pq.offer(Array(nxt, v.toLong, 1L))
            }
          }
        }
      }
    }
    dist(n - 1)(1)
  }
}
