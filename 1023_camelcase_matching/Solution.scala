// LeetCode 1023 - Camelcase Matching
// https://leetcode.com/problems/camelcase-matching/

object Solution {
  def camelMatch(queries: Array[String], pattern: String): Array[Boolean] = {
    def matches(q: String): Boolean = {
      var i = 0
      for (ch <- q) {
        if (i < pattern.length && ch == pattern(i)) i += 1
        else if (ch.isUpper) return false
      }
      i == pattern.length
    }
    queries.map(matches)
  }
}
