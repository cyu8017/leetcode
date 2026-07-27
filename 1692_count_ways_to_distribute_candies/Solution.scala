// LeetCode 1692 - Count Ways to Distribute Candies
// https://leetcode.com/problems/count-ways-to-distribute-candies/

object Solution {
  def waysToDistribute(n: Int, k: Int): Int = {
    val mod = 1000000007
    val dp = Array.fill(k + 1)(0L)
    dp(0) = 1L
    for (i <- 1 to n) {
      val limit = math.min(i, k)
      for (j <- limit to 1 by -1) {
        dp(j) = (dp(j - 1) + j * dp(j)) % mod
      }
      dp(0) = 0L
    }
    dp(k).toInt
  }
}
