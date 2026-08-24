// LeetCode 2850 - Minimum Moves to Spread Stones Over Grid
// https://leetcode.com/problems/minimum-moves-to-spread-stones-over-grid/

object Solution {
  private var extras: scala.collection.mutable.ArrayBuffer[Array[Int]] = _
  private var zeros: scala.collection.mutable.ArrayBuffer[Array[Int]] = _
  private var best: Int = _

  def minimumMoves(grid: Array[Array[Int]]): Int = {
    extras = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    zeros = scala.collection.mutable.ArrayBuffer.empty[Array[Int]]
    for (i <- 0 until 3; j <- 0 until 3) {
      if (grid(i)(j) == 0) zeros += Array(i, j)
      else if (grid(i)(j) > 1) {
        for (_ <- 0 until grid(i)(j) - 1) extras += Array(i, j)
      }
    }
    if (zeros.isEmpty) return 0
    best = 1 << 30
    dfs(0, 0)
    best
  }

  private def dfs(i: Int, cost: Int): Unit = {
    if (cost >= best) return
    if (i == zeros.length) {
      best = cost
      return
    }
    for (j <- extras.indices) {
      if (extras(j)(0) >= 0) {
        val e = extras(j)
        extras(j) = Array(-1, e(1))
        val d = math.abs(e(0) - zeros(i)(0)) + math.abs(e(1) - zeros(i)(1))
        dfs(i + 1, cost + d)
        extras(j) = e
      }
    }
  }
}
