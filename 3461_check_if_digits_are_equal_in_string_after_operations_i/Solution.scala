// LeetCode 3461 - Check If Digits Are Equal in String After Operations I
// https://leetcode.com/problems/check-if-digits-are-equal-in-string-after-operations-i/

object Solution {
  def hasSameDigits(s: String): Boolean = {
    var b = s.toCharArray
    while (b.length > 2) {
      val nb = new Array[Char](b.length - 1)
      var i = 0
      while (i + 1 < b.length) {
        nb(i) = ('0' + (b(i) - '0' + b(i + 1) - '0') % 10).toChar
        i += 1
      }
      b = nb
    }
    b(0) == b(1)
  }
}
