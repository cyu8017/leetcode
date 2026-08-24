// LeetCode 2920 - Maximum Points After Collecting Coins From All Nodes
// https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/

object Solution {
  private var g: Array[scala.collection.mutable.ArrayBuffer[Int]] = _
  private var coins: Array[Int] = _
  private var k: Int = _
  private var memo: scala.collection.mutable.Map[Long, Int] = _

  def maximumPoints(edges: Array[Array[Int]], coins: Array[Int], k: Int): Int = {
    val n = coins.length
    this.coins = coins
    this.k = k
    g = Array.fill(n)(scala.collection.mutable.ArrayBuffer.empty[Int])
    edges.foreach { e =>
      g(e(0)) += e(1)
      g(e(1)) += e(0)
    }
    memo = scala.collection.mutable.Map.empty[Long, Int]
    dfs(0, -1, 0)
  }

  private def dfs(u: Int, p: Int, shifts0: Int): Int = {
    var shifts = shifts0
    if (shifts > 14) shifts = 14
    val key = (u.toLong << 5) | shifts
    if (memo.contains(key)) return memo(key)
    val c = coins(u) >> shifts
    var opt1 = c - k
    var opt2 = c / 2
    g(u).foreach { v =>
      if (v != p) {
        opt1 += dfs(v, u, shifts)
        opt2 += dfs(v, u, shifts + 1)
      }
    }
    val best = math.max(opt1, opt2)
    memo(key) = best
    best
  }
}
