// LeetCode 3734 - Lexicographically Smallest Palindromic Permutation Greater Than Target
// https://leetcode.com/problems/lexicographically-smallest-palindromic-permutation-greater-than-target/

object Solution {
  def lexPalindromicPermutation(s: String, target: String): String = {
    val cnt = Array.fill(26)(0)
    s.foreach(c => cnt(c - 'a') += 1)
    var odd = 0
    var mid = -1
    var i = 0
    while (i < 26) {
      if (cnt(i) % 2 == 1) { odd += 1; mid = i }
      i += 1
    }
    if (odd > 1) return ""
    val half = Array.fill(26)(0)
    i = 0
    while (i < 26) {
      half(i) = cnt(i) / 2
      i += 1
    }
    val n = s.length
    val halfLen = n / 2
    val left = new Array[Char](halfLen)

    def dfs(pos: Int, greater: Boolean): Boolean = {
      if (pos == halfLen) {
        if (mid >= 0) {
          if (greater) return true
          return ('a' + mid).toChar > target.charAt(halfLen)
        }
        return greater
      }
      val start = if (greater) 0 else target.charAt(pos) - 'a'
      var c = start
      while (c < 26) {
        if (half(c) != 0) {
          half(c) -= 1
          left(pos) = ('a' + c).toChar
          if (dfs(pos + 1, greater || c > (target.charAt(pos) - 'a'))) return true
          half(c) += 1
        }
        c += 1
      }
      false
    }

    if (!dfs(0, false)) return ""
    val res = new StringBuilder
    res.append(left)
    if (mid >= 0) res.append(('a' + mid).toChar)
    i = halfLen - 1
    while (i >= 0) {
      res.append(left(i))
      i -= 1
    }
    val out = res.toString
    if (out.compareTo(target) <= 0) "" else out
  }
}
