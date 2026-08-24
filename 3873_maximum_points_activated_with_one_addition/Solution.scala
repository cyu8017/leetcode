// LeetCode 3873 - Maximum Points Activated With One Addition
// https://leetcode.com/problems/maximum-points-activated-with-one-addition/

object Solution {
  private class UnionFind {
    val p = scala.collection.mutable.Map.empty[Long, Long]
    val size = scala.collection.mutable.Map.empty[Long, Int]

    def find(x: Long): Long = {
      if (!p.contains(x)) {
        p(x) = x
        size(x) = 1
      }
      if (p(x) != x) p(x) = find(p(x))
      p(x)
    }

    def unite(a: Long, b: Long): Boolean = {
      var pa = find(a)
      var pb = find(b)
      if (pa == pb) return false
      if (size(pa) > size(pb)) {
        p(pb) = pa
        size(pa) = size(pa) + size(pb)
      } else {
        p(pa) = pb
        size(pb) = size(pb) + size(pa)
      }
      true
    }
  }

  def maxActivated(points: Array[Array[Int]]): Int = {
    val uf = new UnionFind
    val m = 3000000000L
    points.foreach { pt => uf.unite(pt(0).toLong, pt(1).toLong + m) }
    val cnt = scala.collection.mutable.Map.empty[Long, Int]
    points.foreach { pt =>
      val r = uf.find(pt(0).toLong)
      cnt(r) = cnt.getOrElse(r, 0) + 1
    }
    var mx1 = 0
    var mx2 = 0
    cnt.values.foreach { x =>
      if (mx1 < x) { mx2 = mx1; mx1 = x }
      else if (mx2 < x) mx2 = x
    }
    mx1 + mx2 + 1
  }
}
