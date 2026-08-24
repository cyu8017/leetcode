// LeetCode 0685 - Redundant Connection II
// https://leetcode.com/problems/redundant-connection-ii/

object Solution {
  def findRedundantDirectedConnection(edges: Array[Array[Int]]): Array[Int] = {
    val n = edges.length
    val parent = Array.fill(n + 1)(0)
    var cand1: Array[Int] = null
    var cand2: Array[Int] = null
    var i = 0
    while (i < n) {
      val u = edges(i)(0)
      val v = edges(i)(1)
      if (parent(v) == 0) parent(v) = u
      else {
        cand1 = Array(parent(v), v)
        cand2 = Array(u, v)
        edges(i) = Array(-1, -1)
        i = n
      }
      i += 1
    }
    val uf = Array.tabulate(n + 1)(identity)
    def find(x0: Int): Int = {
      var x = x0
      while (uf(x) != x) {
        uf(x) = uf(uf(x))
        x = uf(x)
      }
      x
    }
    for (edge <- edges) {
      if (edge(0) >= 0) {
        val pu = find(edge(0))
        val pv = find(edge(1))
        if (pu == pv) return if (cand1 != null) cand1 else Array(edge(0), edge(1))
        uf(pu) = pv
      }
    }
    cand2
  }
}
