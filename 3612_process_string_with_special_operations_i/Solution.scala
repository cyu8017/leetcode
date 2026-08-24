// LeetCode 3612 - Process String with Special Operations I
// https://leetcode.com/problems/process-string-with-special-operations-i/

object Solution {
  def processStr(s: String): String = {
    val result = new StringBuilder
    s.foreach { c =>
      if (c.isLetter) result.append(c)
      else if (c == '*') {
        if (result.length > 0) result.setLength(result.length - 1)
      } else if (c == '#') result.append(result)
      else if (c == '%') result.reverse()
    }
    result.toString
  }
}
