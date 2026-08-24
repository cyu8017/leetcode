// LeetCode 0790 - Domino and Tromino Tiling
// https://leetcode.com/problems/domino-and-tromino-tiling/

object Solution {
  def numTilings(n: Int): Int = {
    val MOD = 1000000007
    if (n == 1) return 1
    if (n == 2) return 2
    val dp = Array.ofDim[Long](n + 1)
    dp(1) = 1
    dp(2) = 2
    dp(3) = 5
    var i = 4
    while (i <= n) {
      dp(i) = (2 * dp(i - 1) + dp(i - 3)) % MOD
      i += 1
    }
    dp(n).toInt
  }
}
