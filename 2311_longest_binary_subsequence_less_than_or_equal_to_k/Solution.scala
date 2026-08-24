// LeetCode 2311 - Longest Binary Subsequence Less Than or Equal to K
// https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/

object Solution {
  def longestSubsequence(s: String, k: Int): Int = {
    var zeros = 0
    var i = 0
    while (i < s.length) {
      if (s.charAt(i) == '0') zeros += 1
      i += 1
    }
    var value = 0L
    var ones = 0
    var pow = 1L
    i = s.length - 1
    while (i >= 0) {
      if (s.charAt(i) == '1') {
        if (!(pow > k || value + pow > k)) {
          value += pow
          ones += 1
        }
      }
      if (pow <= k) {
        if (pow > (1L << 60)) pow = k + 1L
        else pow <<= 1
      }
      i -= 1
    }
    zeros + ones
  }
}
