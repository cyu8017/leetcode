// LeetCode 2685 - Count the Number of Complete Components
// https://leetcode.com/problems/count-the-number-of-complete-components/

import scala.collection.mutable

object Solution {
  def countCompleteComponents(n: Int, edges: Array[Array[Int]]): Int = {
    val g = Array.fill(n)(mutable.ArrayBuffer.empty[Int])
    var i = 0
    while (i < edges.length) {
      val e = edges(i)
      g(e(0)) += e(1)
      g(e(1)) += e(0)
      i += 1
    }
    val vis = new Array[Boolean](n)
    var ans = 0
    i = 0
    while (i < n) {
      if (!vis(i)) {
        val nodes = mutable.ArrayBuffer.empty[Int]
        dfs(g, vis, i, nodes)
        var ecount = 0
        nodes.foreach(u => ecount += g(u).length)
        ecount /= 2
        val sz = nodes.length
        if (ecount == sz * (sz - 1) / 2) ans += 1
      }
      i += 1
    }
    ans
  }

  private def dfs(
    g: Array[mutable.ArrayBuffer[Int]],
    vis: Array[Boolean],
    u: Int,
    nodes: mutable.ArrayBuffer[Int]
  ): Unit = {
    vis(u) = true
    nodes += u
    g(u).foreach { v =>
      if (!vis(v)) dfs(g, vis, v, nodes)
    }
  }
}
