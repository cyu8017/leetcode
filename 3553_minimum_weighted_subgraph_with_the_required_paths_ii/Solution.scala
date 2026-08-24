// LeetCode 3553 - Minimum Weighted Subgraph With the Required Paths II
// https://leetcode.com/problems/minimum-weighted-subgraph-with-the-required-paths-ii/

object Solution {
  val LOG = 17

  def minimumWeight(edges: Array[Array[Int]], queries: Array[Array[Int]]): Array[Int] = {
    val n = edges.length + 1
    val g = Array.fill(n)(new java.util.ArrayList[Array[Int]]())
    for (e <- edges) {
      g(e(0)).add(Array(e(1), e(2)))
      g(e(1)).add(Array(e(0), e(2)))
    }
    val parent = Array.fill(LOG, n)(-1)
    val depth = new Array[Int](n)
    val dist = new Array[Int](n)

    def dfs(u: Int, p: Int): Unit = {
      parent(0)(u) = p
      val it = g(u).iterator()
      while (it.hasNext) {
        val e = it.next()
        val to = e(0); val w = e(1)
        if (to != p) {
          depth(to) = depth(u) + 1
          dist(to) = dist(u) + w
          dfs(to, u)
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

    def path(u: Int, v: Int): Int = {
      val a = lca(u, v)
      dist(u) + dist(v) - 2 * dist(a)
    }

    dfs(0, -1)
    var k = 1
    while (k < LOG) {
      var v = 0
      while (v < n) {
        if (parent(k - 1)(v) != -1) parent(k)(v) = parent(k - 1)(parent(k - 1)(v))
        v += 1
      }
      k += 1
    }
    val ans = new Array[Int](queries.length)
    var i = 0
    while (i < queries.length) {
      val a = queries(i)(0); val b = queries(i)(1); val c = queries(i)(2)
      ans(i) = (path(a, b) + path(b, c) + path(a, c)) / 2
      i += 1
    }
    ans
  }
}
