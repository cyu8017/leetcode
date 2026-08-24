// LeetCode 3713 - Longest Balanced Substring I
// https://leetcode.com/problems/longest-balanced-substring-i/

object Solution {
  def longestBalanced(s: String): Int = {
    val n = s.length
    var ans = 0
    var i = 0
    while (i < n) {
      val cnt = new Array[Int](26)
      var mx = 0
      var v = 0
      var j = i
      while (j < n) {
        val c = s.charAt(j) - 'a'
        cnt(c) += 1
        if (cnt(c) == 1) v += 1
        mx = math.max(mx, cnt(c))
        if (mx * v == j - i + 1) ans = math.max(ans, j - i + 1)
        j += 1
      }
      i += 1
    }
    ans
  }
}
