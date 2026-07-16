// LeetCode 0008 - String to Integer (atoi)
// https://leetcode.com/problems/string-to-integer-atoi/

object Solution {
  def myAtoi(s: String): Int = {
    var i = 0
    while (i < s.length && s(i) == ' ') i += 1
    if (i >= s.length) return 0

    var sign = 1
    if (s(i) == '-') {
      sign = -1
      i += 1
    } else if (s(i) == '+') {
      i += 1
    }

    var result = 0
    while (i < s.length && s(i).isDigit) {
      val digit = s(i).asDigit
      if (result > (Int.MaxValue - digit) / 10) {
        return if (sign == -1) Int.MinValue else Int.MaxValue
      }
      result = result * 10 + digit
      i += 1
    }

    sign * result
  }
}
