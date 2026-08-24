// LeetCode 3807 - Minimum Cost To Repair Edges To Traverse A Graph
// https://leetcode.com/problems/minimum-cost-to-repair-edges-to-traverse-a-graph/

object Solution {
  def minCost(n: Int, edges: Array[Array[Int]], k: Int): Int = {
    java.util.Arrays.sort(edges, (a: Array[Int], b: Array[Int]) => Integer.compare(a(2), b(2)))
    val m = edges.length
    if (m == 0) return -1

    def check(idx: Int): Boolean = {
      val g = Array.fill(n)(new java.util.ArrayList[Integer]())
      var i = 0
      while (i <= idx) {
        g(edges(i)(0)).add(edges(i)(1))
        g(edges(i)(1)).add(edges(i)(0))
        i += 1
      }
      var q = new java.util.ArrayList[Integer]()
      q.add(0)
      val vis = new Array[Boolean](n)
      vis(0) = true
      var dist = 0
      while (!q.isEmpty) {
        val nq = new java.util.ArrayList[Integer]()
        val it = q.iterator()
        while (it.hasNext) {
          val u = it.next()
          if (u == n - 1) return dist <= k
          val it2 = g(u).iterator()
          while (it2.hasNext) {
            val v = it2.next()
            if (!vis(v)) {
              vis(v) = true
              nq.add(v)
            }
          }
        }
        q = nq
        dist += 1
      }
      false
    }

    var l = 0
    var r = m - 1
    while (l < r) {
      val mid = (l + r) >> 1
      if (check(mid)) r = mid
      else l = mid + 1
    }
    if (check(l)) edges(l)(2) else -1
  }
}
