// LeetCode 3563 - Lexicographically Smallest String After Adjacent Removals
// https://leetcode.com/problems/lexicographically-smallest-string-after-adjacent-removals/

object Solution {
  def isConsec(a: Char, b: Char): Boolean = {
    val d = math.abs(a - b)
    d == 1 || d == 25
  }

  def lexicographicallySmallestString(s: String): String = {
    val n = s.length
    val dp = Array.fill(n + 1, n + 1)("")
    var length = 1
    while (length <= n) {
      var i = 0
      while (i + length <= n) {
        val j = i + length
        var minStr = s.charAt(i) + dp(i + 1)(j)
        var k = i + 1
        while (k < j) {
          if (isConsec(s.charAt(i), s.charAt(k)) && dp(i + 1)(k).isEmpty) {
            val cand = dp(k + 1)(j)
            if (cand.compareTo(minStr) < 0) minStr = cand
          }
          k += 1
        }
        dp(i)(j) = minStr
        i += 1
      }
      length += 1
    }
    dp(0)(n)
  }
}
