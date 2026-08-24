// LeetCode 3614 - Process String with Special Operations II
// https://leetcode.com/problems/process-string-with-special-operations-ii/

object Solution {
  def processStr(s: String, k0: Long): Char = {
    var m = 0L
    s.foreach { c =>
      if (c == '*') m = if (m > 0) m - 1 else 0
      else if (c == '#') m <<= 1
      else if (c != '%') m += 1
    }
    if (k0 >= m) return '.'
    var k = k0
    var i = s.length - 1
    while (true) {
      val c = s.charAt(i)
      if (c == '*') m += 1
      else if (c == '#') {
        m /= 2
        if (k >= m) k -= m
      } else if (c == '%') {
        k = m - 1 - k
      } else {
        m -= 1
        if (k == m) return c
      }
      i -= 1
    }
    '.'
  }
}
