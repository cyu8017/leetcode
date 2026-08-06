// LeetCode 1216 - Valid Palindrome III
// https://leetcode.com/problems/valid-palindrome-iii/

object Solution {
  def isValidPalindrome(s: String, k: Int): Boolean = {
    if (s.isEmpty) return true
    val dp = Array.ofDim[Int](s.length)
    for (i <- s.length - 1 to 0 by -1) {
      var previous = 0
      for (j <- i + 1 until s.length) {
        val old = dp(j)
        if (s(i) == s(j)) dp(j) = previous
        else dp(j) = 1 + math.min(dp(j), dp(j - 1))
        previous = old
      }
    }
    dp.last <= k
  }
}
