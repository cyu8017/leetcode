// LeetCode 2277 - Closest Node to Path in Tree
// https://leetcode.com/problems/closest-node-to-path-in-tree/

object Solution {
  def closestNode(n: Int, edges: Array[Array[Int]], query: Array[Array[Int]]): Array[Int] = {
    val LOG = 17
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- edges) {
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    val up = Array.ofDim[Int](LOG, n)
    val depth = new Array[Int](n)
    def dfs(u: Int, p: Int): Unit = {
      up(0)(u) = p
      for (v <- g(u) if v != p) {
        depth(v) = depth(u) + 1
        dfs(v, u)
      }
    }
    dfs(0, 0)
    var k = 1
    while (k < LOG) {
      var v = 0
      while (v < n) {
        up(k)(v) = up(k - 1)(up(k - 1)(v))
        v += 1
      }
      k += 1
    }
    def lift(v0: Int, d: Int): Int = {
      var v = v0
      var kk = 0
      while (kk < LOG) {
        if (((d >> kk) & 1) != 0) v = up(kk)(v)
        kk += 1
      }
      v
    }
    def lca(a0: Int, b0: Int): Int = {
      var a = a0
      var b = b0
      if (depth(a) < depth(b)) {
        val t = a
        a = b
        b = t
      }
      a = lift(a, depth(a) - depth(b))
      if (a == b) return a
      k = LOG - 1
      while (k >= 0) {
        if (up(k)(a) != up(k)(b)) {
          a = up(k)(a)
          b = up(k)(b)
        }
        k -= 1
      }
      up(0)(a)
    }
    def dist(a: Int, b: Int): Int = {
      val c = lca(a, b)
      depth(a) + depth(b) - 2 * depth(c)
    }
    val ans = new Array[Int](query.length)
    var i = 0
    while (i < query.length) {
      val a = query(i)(0)
      val b = query(i)(1)
      val x = query(i)(2)
      val cands = Array(lca(a, b), lca(a, x), lca(b, x))
      var best = cands(0)
      var bestD = dist(cands(0), x)
      var t = 1
      while (t < 3) {
        val d = dist(cands(t), x)
        if (d < bestD) {
          bestD = d
          best = cands(t)
        }
        t += 1
      }
      ans(i) = best
      i += 1
    }
    ans
  }
}
