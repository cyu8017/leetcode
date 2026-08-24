// LeetCode 3844 - Longest Almost Palindromic Substring
// https://leetcode.com/problems/longest-almost-palindromic-substring/

object Solution {
  def almostPalindromic(s: String): Int = {
    val n = s.length
    var ans = 0
    var i = 0
    while (i < n) {
      ans = math.max(ans, math.max(expand(s, i, i), expand(s, i, i + 1)))
      i += 1
    }
    ans
  }

  private def expand(s: String, l0: Int, r0: Int): Int = {
    val n = s.length
    var l = l0
    var r = r0
    while (l >= 0 && r < n && s.charAt(l) == s.charAt(r)) { l -= 1; r += 1 }
    var l1 = l - 1
    var r1 = r
    var l2 = l
    var r2 = r + 1
    while (l1 >= 0 && r1 < n && s.charAt(l1) == s.charAt(r1)) { l1 -= 1; r1 += 1 }
    while (l2 >= 0 && r2 < n && s.charAt(l2) == s.charAt(r2)) { l2 -= 1; r2 += 1 }
    math.min(n, math.max(r1 - l1 - 1, r2 - l2 - 1))
  }
}
