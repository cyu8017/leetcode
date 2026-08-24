// LeetCode 2060 - Check if an Original String Exists Given Two Encoded Strings
// https://leetcode.com/problems/check-if-an-original-string-exists-given-two-encoded-strings/

object Solution {
  def possiblyEquals(s1: String, s2: String): Boolean = {
    val memo = scala.collection.mutable.Map.empty[(Int, Int, Int), Boolean]
    def isDigit(c: Char): Boolean = c >= '0' && c <= '9'
    def dfs(i: Int, j: Int, diff: Int): Boolean = {
      val key = (i, j, diff)
      if (memo.contains(key)) return memo(key)
      val n = s1.length
      val m = s2.length
      if (i == n && j == m) { memo(key) = diff == 0; return diff == 0 }
      var res = false
      if (diff == 0 && i < n && j < m && !isDigit(s1.charAt(i)) && !isDigit(s2.charAt(j))) {
        if (s1.charAt(i) == s2.charAt(j)) res = dfs(i + 1, j + 1, 0)
      } else if (diff > 0 && i < n && !isDigit(s1.charAt(i))) {
        res = dfs(i + 1, j, diff - 1)
      } else if (diff < 0 && j < m && !isDigit(s2.charAt(j))) {
        res = dfs(i, j + 1, diff + 1)
      }
      if (!res && i < n && isDigit(s1.charAt(i))) {
        var value = 0
        var p = i
        var stop = false
        while (!stop && p < n && isDigit(s1.charAt(p))) {
          value = value * 10 + (s1.charAt(p) - '0')
          if (dfs(p + 1, j, diff + value)) { res = true; stop = true }
          p += 1
        }
      }
      if (!res && j < m && isDigit(s2.charAt(j))) {
        var value = 0
        var p = j
        var stop = false
        while (!stop && p < m && isDigit(s2.charAt(p))) {
          value = value * 10 + (s2.charAt(p) - '0')
          if (dfs(i, p + 1, diff - value)) { res = true; stop = true }
          p += 1
        }
      }
      memo(key) = res
      res
    }
    dfs(0, 0, 0)
  }
}
