// LeetCode 2973 - Find Number of Coins to Place in Tree Nodes
// https://leetcode.com/problems/find-number-of-coins-to-place-in-tree-nodes/

object Solution {
  def placedCoins(edges: Array[Array[Int]], cost: Array[Int]): Array[Long] = {
    val n = cost.length
    val g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    for (e <- edges) {
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    val ans = Array.ofDim[Long](n)

    def dfs(u: Int, p: Int): scala.collection.mutable.ArrayBuffer[Int] = {
      val vals = scala.collection.mutable.ArrayBuffer[Int](cost(u))
      for (v <- g(u) if v != p) vals ++= dfs(v, u)
      val sorted = vals.sorted
      if (sorted.length < 3) ans(u) = 1
      else {
        val m = sorted.length
        val cand1 = sorted(m - 1).toLong * sorted(m - 2) * sorted(m - 3)
        val cand2 = sorted(0).toLong * sorted(1) * sorted(m - 1)
        var best = math.max(cand1, cand2)
        if (best < 0) best = 0
        ans(u) = best
      }
      if (sorted.length <= 5) sorted
      else scala.collection.mutable.ArrayBuffer(sorted(0), sorted(1), sorted(sorted.length - 3), sorted(sorted.length - 2), sorted(sorted.length - 1))
    }

    dfs(0, -1)
    ans
  }
}
