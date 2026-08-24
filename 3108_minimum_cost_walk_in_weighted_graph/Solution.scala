// LeetCode 3108 - Minimum Cost Walk in Weighted Graph
// https://leetcode.com/problems/minimum-cost-walk-in-weighted-graph/

object Solution {
  private class UnionFind(n: Int) {
    val p: Array[Int] = Array.tabulate(n)(i => i)
    val size: Array[Int] = Array.fill(n)(1)

    def find(x: Int): Int = {
      if (p(x) != x) p(x) = find(p(x))
      p(x)
    }

    def unite(a: Int, b: Int): Unit = {
      val pa = find(a)
      val pb = find(b)
      if (pa == pb) return
      if (size(pa) > size(pb)) {
        p(pb) = pa
        size(pa) += size(pb)
      } else {
        p(pa) = pb
        size(pb) += size(pa)
      }
    }
  }

  def minimumCost(n: Int, edges: Array[Array[Int]], query: Array[Array[Int]]): Array[Int] = {
    val uf = new UnionFind(n)
    val g = Array.fill(n)(-1)
    edges.foreach(e => uf.unite(e(0), e(1)))
    edges.foreach { e =>
      val root = uf.find(e(0))
      g(root) &= e(2)
    }
    val ans = new Array[Int](query.length)
    var i = 0
    while (i < query.length) {
      val u = query(i)(0)
      val v = query(i)(1)
      if (u == v) ans(i) = 0
      else {
        val a = uf.find(u)
        val b = uf.find(v)
        ans(i) = if (a == b) g(a) else -1
      }
      i += 1
    }
    ans
  }
}
