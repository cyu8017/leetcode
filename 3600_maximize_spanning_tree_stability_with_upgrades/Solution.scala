// LeetCode 3600 - Maximize Spanning Tree Stability with Upgrades
// https://leetcode.com/problems/maximize-spanning-tree-stability-with-upgrades/

object Solution {
  class UnionFind(n: Int) {
    val p = Array.tabulate(n)(i => i)
    val size = Array.fill(n)(1)
    var cnt = n

    def find(x0: Int): Int = {
      var x = x0
      if (p(x) != x) p(x) = find(p(x))
      p(x)
    }

    def unite(a: Int, b: Int): Boolean = {
      var pa = find(a)
      var pb = find(b)
      if (pa == pb) return false
      if (size(pa) > size(pb)) {
        p(pb) = pa
        size(pa) += size(pb)
      } else {
        p(pa) = pb
        size(pb) += size(pa)
      }
      cnt -= 1
      true
    }
  }

  def maxStability(n: Int, edges: Array[Array[Int]], k: Int): Int = {
    def check(lim: Int): Boolean = {
      val uf = new UnionFind(n)
      for (e <- edges) if (e(2) >= lim) uf.unite(e(0), e(1))
      var rem = k
      for (e <- edges) {
        if (e(2) * 2 >= lim && rem > 0) {
          if (uf.unite(e(0), e(1))) rem -= 1
        }
      }
      uf.cnt == 1
    }

    val uf = new UnionFind(n)
    var mn = 1000000
    for (e <- edges) {
      if (e(3) == 1) {
        mn = math.min(mn, e(2))
        if (!uf.unite(e(0), e(1))) return -1
      }
    }
    for (e <- edges) uf.unite(e(0), e(1))
    if (uf.cnt > 1) return -1
    var l = 1
    var r = mn
    while (l < r) {
      val mid = (l + r + 1) >> 1
      if (check(mid)) l = mid
      else r = mid - 1
    }
    l
  }
}
