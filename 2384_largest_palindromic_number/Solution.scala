// LeetCode 2384 - Largest Palindromic Number
// https://leetcode.com/problems/largest-palindromic-number/

object Solution {
  def largestPalindromic(num: String): String = {
    val freq = Array.fill(10)(0)
    var i = 0
    while (i < num.length) {
      freq(num.charAt(i) - '0') += 1
      i += 1
    }
    val left = new StringBuilder
    var d = 9
    while (d >= 0) {
      val pairs = freq(d) / 2
      var p = 0
      while (p < pairs) {
        left.append(('0' + d).toChar)
        p += 1
      }
      freq(d) %= 2
      d -= 1
    }
    var mid = 0.toChar
    d = 9
    while (d >= 0) {
      if (freq(d) > 0) {
        mid = ('0' + d).toChar
        d = -1
      } else d -= 1
    }
    if (left.length == 0 || left.charAt(0) == '0') {
      return if (mid == 0) "0" else mid.toString
    }
    val ans = new StringBuilder(left.toString)
    if (mid != 0) ans.append(mid)
    ans.append(left.reverse())
    ans.toString
  }
}
