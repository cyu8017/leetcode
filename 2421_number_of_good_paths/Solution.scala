// LeetCode 2421 - Number of Good Paths
// https://leetcode.com/problems/number-of-good-paths/

object Solution {
  def numberOfGoodPaths(vals: Array[Int], edges: Array[Array[Int]]): Int = {
    val n = vals.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    val parent = Array.tabulate(n)(identity)
    val size = Array.fill(n)(1)

    def find(x: Int): Int = {
      if (parent(x) != x) parent(x) = find(parent(x))
      parent(x)
    }

    val nodes = Array.tabulate(n)(identity)
    scala.util.Sorting.stableSort(nodes, (a: Int, b: Int) => vals(a) < vals(b) || (vals(a) == vals(b) && a < b))
    var ans = n
    var i = 0
    while (i < n) {
      var j = i
      while (j < n && vals(nodes(j)) == vals(nodes(i))) j += 1
      var k = i
      while (k < j) {
        val u = nodes(k)
        g(u).foreach { v =>
          if (vals(v) <= vals(u)) {
            val ru = find(u)
            val rv = find(v)
            if (ru != rv) {
              parent(ru) = rv
              size(rv) += size(ru)
            }
          }
        }
        k += 1
      }
      val freq = scala.collection.mutable.Map.empty[Int, Int]
      k = i
      while (k < j) {
        val r = find(nodes(k))
        freq(r) = freq.getOrElse(r, 0) + 1
        k += 1
      }
      freq.values.foreach { c => ans += c * (c - 1) / 2 }
      i = j
    }
    ans
  }
}
