// LeetCode 2846 - Minimum Edge Weight Equilibrium Queries in a Tree
// https://leetcode.com/problems/minimum-edge-weight-equilibrium-queries-in-a-tree/

object Solution {
  private val LOG = 15
  private var g: Array[scala.collection.mutable.ArrayBuffer[Array[Int]]] = _
  private var up: Array[Array[Int]] = _
  private var depth: Array[Int] = _
  private var cnt: Array[Array[Int]] = _

  def minOperationsQueries(n: Int, edges: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Array[Int]])
    edges.foreach { e =>
      g(e(0)) += Array(e(1), e(2))
      g(e(1)) += Array(e(0), e(2))
    }
    up = Array.ofDim[Int](LOG, n)
    depth = Array.fill(n)(0)
    cnt = Array.ofDim[Int](n, 27)
    dfs(0, 0)
    for (j <- 1 until LOG; i <- 0 until n) up(j)(i) = up(j - 1)(up(j - 1)(i))
    queries.map { q =>
      val a = q(0)
      val b = q(1)
      val c = lca(a, b)
      val total = depth(a) + depth(b) - 2 * depth(c)
      var best = 0
      for (w <- 1 to 26) {
        val f = cnt(a)(w) + cnt(b)(w) - 2 * cnt(c)(w)
        best = math.max(best, f)
      }
      total - best
    }
  }

  private def dfs(u: Int, p: Int): Unit = {
    up(0)(u) = p
    g(u).foreach { e =>
      val v = e(0)
      val w = e(1)
      if (v != p) {
        depth(v) = depth(u) + 1
        Array.copy(cnt(u), 0, cnt(v), 0, 27)
        cnt(v)(w) += 1
        dfs(v, u)
      }
    }
  }

  private def lca(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    if (depth(a) < depth(b)) {
      val t = a
      a = b
      b = t
    }
    val diff = depth(a) - depth(b)
    for (j <- 0 until LOG) if ((diff & (1 << j)) != 0) a = up(j)(a)
    if (a == b) return a
    for (j <- LOG - 1 to 0 by -1) {
      if (up(j)(a) != up(j)(b)) {
        a = up(j)(a)
        b = up(j)(b)
      }
    }
    up(0)(a)
  }
}
