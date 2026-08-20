// LeetCode 1269 - Number of Ways to Stay in the Same Place After Some Steps
// https://leetcode.com/problems/number-of-ways-to-stay-in-the-same-place-after-some-steps/

object Solution {
  def numWays(steps: Int, arrLen: Int): Int = {
    val mod = 1000000007
    val width = math.min(arrLen, steps / 2 + 1)
    var dp = Array.fill(width)(0)
    dp(0) = 1
    for (_ <- 0 until steps) {
      dp = Array.tabulate(width) { i =>
        var v = dp(i).toLong
        if (i > 0) v += dp(i - 1)
        if (i + 1 < width) v += dp(i + 1)
        (v % mod).toInt
      }
    }
    dp(0)
  }
}
