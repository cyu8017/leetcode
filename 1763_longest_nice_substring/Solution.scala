// LeetCode 1763 - Longest Nice Substring
// https://leetcode.com/problems/longest-nice-substring/

object Solution {
  def longestNiceSubstring(s: String): String = {
    var bestStart = 0
    var bestLen = 0
    for (i <- s.indices) {
      var lower = 0
      var upper = 0
      for (j <- i until s.length) {
        val c = s(j)
        if (c.isLower) {
          lower |= 1 << (c - 'a')
        } else {
          upper |= 1 << (c - 'A')
        }
        if (lower == upper && j - i + 1 > bestLen) {
          bestStart = i
          bestLen = j - i + 1
        }
      }
    }
    s.substring(bestStart, bestStart + bestLen)
  }
}
