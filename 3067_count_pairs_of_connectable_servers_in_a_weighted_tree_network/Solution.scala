// LeetCode 3067 - Count Pairs of Connectable Servers in a Weighted Tree Network
// https://leetcode.com/problems/count-pairs-of-connectable-servers-in-a-weighted-tree-network/

object Solution {
  def countPairsOfConnectableServers(edges: Array[Array[Int]], signalSpeed: Int): Array[Int] = {
    val n = edges.length + 1
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Array[Int]])
    edges.foreach { e =>
      g(e(0)) += Array(e(1), e(2))
      g(e(1)) += Array(e(0), e(2))
    }

    def dfs(a: Int, fa: Int, ws: Int): Int = {
      var cnt = if (ws % signalSpeed == 0) 1 else 0
      g(a).foreach { e =>
        val b = e(0)
        val w = e(1)
        if (b != fa) cnt += dfs(b, a, ws + w)
      }
      cnt
    }

    val ans = new Array[Int](n)
    var a = 0
    while (a < n) {
      var s = 0
      g(a).foreach { e =>
        val t = dfs(e(0), a, e(1))
        ans(a) += s * t
        s += t
      }
      a += 1
    }
    ans
  }
}
