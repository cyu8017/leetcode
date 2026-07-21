// LeetCode 1866 - Number of Ways to Rearrange Sticks With K Sticks Visible
// https://leetcode.com/problems/number-of-ways-to-rearrange-sticks-with-k-sticks-visible/

object Solution {
  def rearrangeSticks(n: Int, k: Int): Int = {
    val mod = 1000000007
    if (k == 0 || k > n) return 0
    val dp = Array.fill(n + 1, n + 1)(0L)
    dp(1)(1) = 1
    for (sticks <- 2 to n) {
      dp(sticks)(1) = (sticks - 1) * dp(sticks - 1)(1) % mod
      for (visible <- 2 to sticks) {
        dp(sticks)(visible) = (
          dp(sticks - 1)(visible - 1) + (sticks - 1) * dp(sticks - 1)(visible)
        ) % mod
      }
    }
    dp(n)(k).toInt
  }
}
