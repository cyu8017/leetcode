// LeetCode 1230 - Toss Strange Coins
// https://leetcode.com/problems/toss-strange-coins/

object Solution {
  def probabilityOfHeads(prob: Array[Double], target: Int): Double = {
    val dp = Array.fill(target + 1)(0.0)
    dp(0) = 1.0
    for (p <- prob) {
      for (heads <- target to 0 by -1) {
        dp(heads) = dp(heads) * (1 - p) + (if (heads > 0) dp(heads - 1) * p else 0.0)
      }
    }
    dp(target)
  }
}
