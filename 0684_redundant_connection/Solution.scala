// LeetCode 0684 - Redundant Connection
// https://leetcode.com/problems/redundant-connection/

object Solution {
  def findRedundantConnection(edges: Array[Array[Int]]): Array[Int] = {
    val parent = Array.tabulate(edges.length + 1)(identity)
    def find(x0: Int): Int = {
      var x = x0
      while (parent(x) != x) {
        parent(x) = parent(parent(x))
        x = parent(x)
      }
      x
    }
    for (edge <- edges) {
      val u = edge(0)
      val v = edge(1)
      val pu = find(u)
      val pv = find(v)
      if (pu == pv) return Array(u, v)
      parent(pu) = pv
    }
    Array.empty[Int]
  }
}
