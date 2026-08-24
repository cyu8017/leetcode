// LeetCode 2533 - Number of Good Binary Strings
// https://leetcode.com/problems/number-of-good-binary-strings/

object Solution {
  def goodBinaryStrings(minLength: Int, maxLength: Int, oneGroup: Int, zeroGroup: Int): Int = {
    val MOD = 1000000007
    val dp = Array.fill(maxLength + 1)(0)
    dp(0) = 1
    var i = 0
    while (i <= maxLength) {
      if (dp(i) != 0) {
        if (i + oneGroup <= maxLength) dp(i + oneGroup) = (dp(i + oneGroup) + dp(i)) % MOD
        if (i + zeroGroup <= maxLength) dp(i + zeroGroup) = (dp(i + zeroGroup) + dp(i)) % MOD
      }
      i += 1
    }
    var ans = 0
    i = minLength
    while (i <= maxLength) {
      ans = (ans + dp(i)) % MOD
      i += 1
    }
    ans
  }
}
