// LeetCode 3559 - Number of Ways to Assign Edge Weights II
// https://leetcode.com/problems/number-of-ways-to-assign-edge-weights-ii/

object Solution {
  val MOD = 1000000007
  val LOG = 17

  def assignEdgeWeights(edges: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    val n = edges.length + 1
    val depth = new Array[Int](n + 1)
    val graph = Array.fill(n + 1)(new java.util.ArrayList[Integer]())
    val parent = Array.fill(LOG, n + 1)(-1)
    for (e <- edges) {
      graph(e(0)).add(e(1))
      graph(e(1)).add(e(0))
    }

    def dfs(u: Int, p: Int): Unit = {
      parent(0)(u) = p
      val it = graph(u).iterator()
      while (it.hasNext) {
        val v = it.next().intValue()
        if (v != p) {
          depth(v) = depth(u) + 1
          dfs(v, u)
        }
      }
    }

    def lca(u0: Int, v0: Int): Int = {
      var u = u0
      var v = v0
      if (depth(u) < depth(v)) { val t = u; u = v; v = t }
      var k = LOG - 1
      while (k >= 0) {
        if (parent(k)(u) != -1 && depth(parent(k)(u)) >= depth(v)) u = parent(k)(u)
        k -= 1
      }
      if (u == v) return u
      k = LOG - 1
      while (k >= 0) {
        if (parent(k)(u) != -1 && parent(k)(u) != parent(k)(v)) {
          u = parent(k)(u)
          v = parent(k)(v)
        }
        k -= 1
      }
      parent(0)(u)
    }

    def modPow(exp0: Int): Int = {
      var exp = exp0
      var base = 2L
      var res = 1L
      while (exp > 0) {
        if ((exp & 1) != 0) res = res * base % MOD
        base = base * base % MOD
        exp >>= 1
      }
      res.toInt
    }

    dfs(1, -1)
    var k = 1
    while (k < LOG) {
      var v = 1
      while (v <= n) {
        if (parent(k - 1)(v) != -1) parent(k)(v) = parent(k - 1)(parent(k - 1)(v))
        v += 1
      }
      k += 1
    }
    val ans = new Array[Int](queries.length)
    var i = 0
    while (i < queries.length) {
      val u = queries(i)(0)
      val v = queries(i)(1)
      if (u == v) ans(i) = 0
      else {
        val a = lca(u, v)
        val d = depth(u) + depth(v) - 2 * depth(a)
        ans(i) = modPow(d - 1)
      }
      i += 1
    }
    ans
  }
}
