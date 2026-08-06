// LeetCode 1223 - Dice Roll Simulation
// https://leetcode.com/problems/dice-roll-simulation/

object Solution {
  def dieSimulator(n: Int, rollMax: Array[Int]): Int = {
    val mod = 1000000007
    var dp = Array.tabulate(6)(j => Array.fill(rollMax(j) + 1)(0))
    for (j <- 0 until 6) dp(j)(1) = 1
    for (_ <- 1 until n) {
      val totals = dp.map(_.sum % mod)
      val totalSum = totals.sum % mod
      val nxt = Array.tabulate(6)(j => Array.fill(dp(j).length)(0))
      for (j <- 0 until 6) {
        nxt(j)(1) = ((totalSum - totals(j)) % mod + mod) % mod
        for (run <- 2 until dp(j).length) nxt(j)(run) = dp(j)(run - 1)
      }
      dp = nxt
    }
    (dp.map(_.sum.toLong).sum % mod).toInt
  }
}
