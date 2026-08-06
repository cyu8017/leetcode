// LeetCode 1147 - Longest Chunked Palindrome Decomposition
// https://leetcode.com/problems/longest-chunked-palindrome-decomposition/

object Solution {
  def longestDecomposition(text: String): Int = {
    val n = text.length
    var ans = 0
    var i = 0
    while (i < n - i) {
      var found = false
      var length = 1
      val limit = (n - 2 * i) / 2
      while (length <= limit && !found) {
        if (text.substring(i, i + length) == text.substring(n - i - length, n - i)) {
          ans += 2
          i += length
          found = true
        } else length += 1
      }
      if (!found) {
        ans += 1
        return ans
      }
    }
    ans
  }
}
