// LeetCode 1761 - Minimum Degree of a Connected Trio in a Graph
// https://leetcode.com/problems/minimum-degree-of-a-connected-trio-in-a-graph/

object Solution {
  def minTrioDegree(n: Int, edges: Array[Array[Int]]): Int = {
    val adj = Array.ofDim[Boolean](n, n)
    val degree = new Array[Int](n)
    for (e <- edges) {
      val u = e(0) - 1
      val v = e(1) - 1
      adj(u)(v) = true
      adj(v)(u) = true
      degree(u) += 1
      degree(v) += 1
    }
    var best = Int.MaxValue
    for (e <- edges) {
      val u = e(0) - 1
      val v = e(1) - 1
      for (k <- 0 until n) {
        if (adj(u)(k) && adj(v)(k)) {
          best = math.min(best, degree(u) + degree(v) + degree(k) - 6)
        }
      }
    }
    if (best == Int.MaxValue) -1 else best
  }
}
