// LeetCode 0738 - Monotone Increasing Digits
// https://leetcode.com/problems/monotone-increasing-digits/

object Solution {
  def monotoneIncreasingDigits(n: Int): Int = {
    val digits = n.toString.toCharArray
    var mark = digits.length
    var i = digits.length - 1
    while (i > 0) {
      if (digits(i) < digits(i - 1)) {
        digits(i - 1) = (digits(i - 1) - 1).toChar
        mark = i
      }
      i -= 1
    }
    i = mark
    while (i < digits.length) {
      digits(i) = '9'
      i += 1
    }
    new String(digits).toInt
  }
}
