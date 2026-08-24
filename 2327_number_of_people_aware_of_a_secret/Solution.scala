// LeetCode 2327 - Number of People Aware of a Secret
// https://leetcode.com/problems/number-of-people-aware-of-a-secret/

object Solution {
  def peopleAwareOfSecret(n: Int, delay: Int, forget: Int): Int = {
    val mod = 1000000007
    val dp = Array.fill(n + 1)(0)
    dp(1) = 1
    var share = 0
    var day = 2
    while (day <= n) {
      if (day - delay >= 1) share = (share + dp(day - delay)) % mod
      if (day - forget >= 1) share = (share - dp(day - forget) + mod) % mod
      dp(day) = share
      day += 1
    }
    var ans = 0
    day = n - forget + 1
    while (day <= n) {
      if (day >= 1) ans = (ans + dp(day)) % mod
      day += 1
    }
    ans
  }
}
