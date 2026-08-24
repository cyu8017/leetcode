// LeetCode 2858 - Minimum Edge Reversals So Every Node Is Reachable
// https://leetcode.com/problems/minimum-edge-reversals-so-every-node-is-reachable/

object Solution {
  private var g: Array[scala.collection.mutable.ArrayBuffer[Array[Int]]] = _
  private var ans: Array[Int] = _

  def minEdgeReversals(n: Int, edges: Array[Array[Int]]): Array[Int] = {
    g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Array[Int]])
    edges.foreach { e =>
      val u = e(0)
      val v = e(1)
      g(u) += Array(v, 0)
      g(v) += Array(u, 1)
    }
    ans = Array.fill(n)(0)
    dfs1(0, -1)
    dfs2(0, -1)
    ans
  }

  private def dfs1(u: Int, p: Int): Unit = {
    g(u).foreach { e =>
      val v = e(0)
      val ww = e(1)
      if (v != p) {
        ans(0) += ww
        dfs1(v, u)
      }
    }
  }

  private def dfs2(u: Int, p: Int): Unit = {
    g(u).foreach { e =>
      val v = e(0)
      val ww = e(1)
      if (v != p) {
        ans(v) = if (ww == 0) ans(u) + 1 else ans(u) - 1
        dfs2(v, u)
      }
    }
  }
}
