// LeetCode 0651 - 4 Keys Keyboard
// https://leetcode.com/problems/4-keys-keyboard/

object Solution {
  def maxA(n: Int): Int = {
    val dp = Array.tabulate(n + 1)(identity)
    var i = 1
    while (i <= n) {
      var j = 0
      while (j < i - 2) {
        dp(i) = math.max(dp(i), dp(j) * (i - j - 1))
        j += 1
      }
      i += 1
    }
    dp(n)
  }
}
