// LeetCode 3608 - Minimum Time for K Connected Components
// https://leetcode.com/problems/minimum-time-for-k-connected-components/

object Solution {
  class UnionFind(n: Int) {
    val p = Array.tabulate(n)(i => i)
    val size = Array.fill(n)(1)

    def find(x0: Int): Int = {
      var x = x0
      if (p(x) != x) p(x) = find(p(x))
      p(x)
    }

    def unite(a: Int, b: Int): Boolean = {
      val pa = find(a)
      val pb = find(b)
      if (pa == pb) return false
      if (size(pa) > size(pb)) {
        p(pb) = pa
        size(pa) += size(pb)
      } else {
        p(pa) = pb
        size(pb) += size(pa)
      }
      true
    }
  }

  def minTime(n: Int, edges: Array[Array[Int]], k: Int): Int = {
    java.util.Arrays.sort(edges, (a: Array[Int], b: Array[Int]) => Integer.compare(a(2), b(2)))
    val uf = new UnionFind(n)
    var cnt = n
    var i = edges.length - 1
    while (i >= 0) {
      if (uf.unite(edges(i)(0), edges(i)(1))) {
        cnt -= 1
        if (cnt < k) return edges(i)(2)
      }
      i -= 1
    }
    0
  }
}
