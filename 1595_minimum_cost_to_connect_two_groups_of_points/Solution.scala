// LeetCode 1595 - Minimum Cost to Connect Two Groups of Points
// https://leetcode.com/problems/minimum-cost-to-connect-two-groups-of-points/

object Solution {
  def connectTwoGroups(cost: Array[Array[Int]]): Int = {
    val m = cost.length
    val n = cost(0).length
    val full = 1 << n
    val inf = 1000000000
    var dp = Array.fill(full)(inf)
    dp(0) = 0
    for (row <- cost) {
      val nxt = Array.fill(full)(inf)
      for (mask <- 0 until full; j <- 0 until n) {
        val newMask = mask | (1 << j)
        nxt(newMask) = math.min(nxt(newMask), math.min(dp(mask) + row(j), nxt(mask) + row(j)))
      }
      dp = nxt
    }
    val minimum = Array.tabulate(n)(j => (0 until m).map(i => cost(i)(j)).min)
    (0 until full).map { mask =>
      dp(mask) + (0 until n).filter(j => ((mask >> j) & 1) == 0).map(minimum).sum
    }.min
  }
}
