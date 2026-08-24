// LeetCode 3604 - Minimum Time to Reach Destination in Directed Graph
// https://leetcode.com/problems/minimum-time-to-reach-destination-in-directed-graph/

object Solution {
  def minTime(n: Int, edges: Array[Array[Int]]): Int = {
    val g = Array.fill(n)(new java.util.ArrayList[Array[Int]]())
    for (e <- edges) g(e(0)).add(Array(e(1), e(2), e(3)))
    val Inf = 1000000000000000000L
    val dist = Array.fill(n)(Inf)
    dist(0) = 0
    val pq = new java.util.PriorityQueue[Array[Long]]((a: Array[Long], b: Array[Long]) => java.lang.Long.compare(a(0), b(0)))
    pq.offer(Array(0L, 0L))
    while (!pq.isEmpty) {
      val cur = pq.poll()
      val t = cur(0)
      val u = cur(1).toInt
      if (t == dist(u)) {
        if (u == n - 1) return t.toInt
        val it = g(u).iterator()
        while (it.hasNext) {
          val e = it.next()
          var nt = t
          if (nt <= e(2)) {
            if (nt < e(1)) nt = e(1)
            nt += 1
            if (nt < dist(e(0))) {
              dist(e(0)) = nt
              pq.offer(Array(nt, e(0).toLong))
            }
          }
        }
      }
    }
    if (dist(n - 1) == Inf) -1 else dist(n - 1).toInt
  }
}
