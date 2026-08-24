// LeetCode 3504 - Longest Palindrome After Substring Concatenation II
// https://leetcode.com/problems/longest-palindrome-after-substring-concatenation-ii/

object Solution {
  def expand(s: String, g: Array[Int], l0: Int, r0: Int): Unit = {
    var l = l0
    var r = r0
    while (l >= 0 && r < s.length && s.charAt(l) == s.charAt(r)) {
      g(l) = math.max(g(l), r - l + 1)
      l -= 1
      r += 1
    }
  }

  def calc(s: String): Array[Int] = {
    val n = s.length
    val g = new Array[Int](n)
    var i = 0
    while (i < n) {
      expand(s, g, i, i)
      expand(s, g, i, i + 1)
      i += 1
    }
    g
  }

  def longestPalindrome(s: String, t0: String): Int = {
    val m = s.length
    val n = t0.length
    val tc = t0.toCharArray
    var _i = 0
    var _j = tc.length - 1
    while (_i < _j) {
      val tmp = tc(_i)
      tc(_i) = tc(_j)
      tc(_j) = tmp
      _i += 1
      _j -= 1
    }
    val t = new String(tc)
    val g1 = calc(s)
    val g2 = calc(t)
    var ans = 0
    for (v <- g1) ans = math.max(ans, v)
    for (v <- g2) ans = math.max(ans, v)
    val f = Array.ofDim[Int](m + 1, n + 1)
    var i = 1
    while (i <= m) {
      var j = 1
      while (j <= n) {
        if (s.charAt(i - 1) == t.charAt(j - 1)) {
          f(i)(j) = f(i - 1)(j - 1) + 1
          val a = if (i < m) g1(i) else 0
          val b = if (j < n) g2(j) else 0
          ans = math.max(ans, f(i)(j) * 2 + a)
          ans = math.max(ans, f(i)(j) * 2 + b)
        }
        j += 1
      }
      i += 1
    }
    ans
  }
}
