// LeetCode 1140 - Stone Game II
// https://leetcode.com/problems/stone-game-ii/

object Solution {
  def stoneGameII(piles: Array[Int]): Int = {
    val n = piles.length
    val suffix = Array.ofDim[Int](n + 1)
    for (i <- n - 1 to 0 by -1) suffix(i) = suffix(i + 1) + piles(i)
    val memo = scala.collection.mutable.Map.empty[(Int, Int), Int]
    def dfs(i: Int, m: Int): Int = {
      if (i >= n) return 0
      if (i + m >= n) return suffix(i)
      memo.getOrElseUpdate((i, m), {
        var minOpp = Int.MaxValue
        for (x <- 1 to math.min(2 * m, n - i)) {
          minOpp = math.min(minOpp, dfs(i + x, math.max(x, m)))
        }
        suffix(i) - minOpp
      })
    }
    dfs(0, 1)
  }
}
