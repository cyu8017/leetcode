// LeetCode 2585 - Number of Ways to Earn Points
// https://leetcode.com/problems/number-of-ways-to-earn-points/

object Solution {
  def waysToReachTarget(target: Int, types: Array[Array[Int]]): Int = {
    val MOD = 1000000007
    val dp = Array.fill(target + 1)(0)
    dp(0) = 1
    types.foreach { t =>
      val count = t(0)
      val marks = t(1)
      var s = target
      while (s >= 0) {
        var k = 1
        while (k <= count && s - k * marks >= 0) {
          dp(s) = (dp(s) + dp(s - k * marks)) % MOD
          k += 1
        }
        s -= 1
      }
    }
    dp(target)
  }
}
