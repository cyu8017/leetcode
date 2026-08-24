// LeetCode 2466 - Count Ways To Build Good Strings
// https://leetcode.com/problems/count-ways-to-build-good-strings/

object Solution {
  def countGoodStrings(low: Int, high: Int, zero: Int, one: Int): Int = {
    val mod = 1000000007
    val dp = new Array[Int](high + 1)
    dp(0) = 1
    var ans = 0
    var i = 1
    while (i <= high) {
      if (i >= zero) dp(i) = (dp(i) + dp(i - zero)) % mod
      if (i >= one) dp(i) = (dp(i) + dp(i - one)) % mod
      if (i >= low) ans = (ans + dp(i)) % mod
      i += 1
    }
    ans
  }
}
