// LeetCode 0005 - Longest Palindromic Substring
// https://leetcode.com/problems/longest-palindromic-substring/

object Solution {
  def longestPalindrome(s: String): String = {
    var bestStart = 0
    var bestLen = 0

    def expand(left: Int, right: Int): Unit = {
      var l = left
      var r = right
      while (l >= 0 && r < s.length && s(l) == s(r)) {
        l -= 1
        r += 1
      }
      val len = r - l - 1
      if (len > bestLen) {
        bestLen = len
        bestStart = l + 1
      }
    }

    s.indices.foreach { i =>
      expand(i, i)
      expand(i, i + 1)
    }

    s.substring(bestStart, bestStart + bestLen)
  }
}
