// LeetCode 2316 - Count Unreachable Pairs of Nodes in an Undirected Graph
// https://leetcode.com/problems/count-unreachable-pairs-of-nodes-in-an-undirected-graph/

object Solution {
  def countPairs(n: Int, edges: Array[Array[Int]]): Long = {
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    val vis = Array.fill(n)(false)

    def dfs(u: Int): Int = {
      vis(u) = true
      var size = 1
      g(u).foreach { v =>
        if (!vis(v)) size += dfs(v)
      }
      size
    }

    var ans = 0L
    var seen = 0L
    var i = 0
    while (i < n) {
      if (!vis(i)) {
        val sz = dfs(i).toLong
        ans += sz * seen
        seen += sz
      }
      i += 1
    }
    ans
  }
}
