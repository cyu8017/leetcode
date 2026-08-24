// LeetCode 2472 - Maximum Number of Non-overlapping Palindrome Substrings
// https://leetcode.com/problems/maximum-number-of-non-overlapping-palindrome-substrings/

object Solution {
  def maxPalindromes(s: String, k: Int): Int = {
    val n = s.length
    val isPal = Array.ofDim[Boolean](n, n)
    var i = 0
    while (i < n) {
      isPal(i)(i) = true
      i += 1
    }
    i = 0
    while (i + 1 < n) {
      isPal(i)(i + 1) = s.charAt(i) == s.charAt(i + 1)
      i += 1
    }
    var length = 3
    while (length <= n) {
      i = 0
      while (i + length - 1 < n) {
        val j = i + length - 1
        isPal(i)(j) = s.charAt(i) == s.charAt(j) && isPal(i + 1)(j - 1)
        i += 1
      }
      length += 1
    }
    val dp = new Array[Int](n + 1)
    i = n - 1
    while (i >= 0) {
      dp(i) = dp(i + 1)
      var j = i + k - 1
      while (j < n) {
        if (isPal(i)(j) && 1 + dp(j + 1) > dp(i)) dp(i) = 1 + dp(j + 1)
        j += 1
      }
      i -= 1
    }
    dp(0)
  }
}
