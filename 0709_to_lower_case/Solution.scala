// LeetCode 0709 - To Lower Case
// https://leetcode.com/problems/to-lower-case/

object Solution {
  def toLowerCase(s: String): String = {
    val chars = s.toCharArray
    var i = 0
    while (i < chars.length) {
      if (chars(i) >= 'A' && chars(i) <= 'Z') chars(i) = (chars(i) + 32).toChar
      i += 1
    }
    new String(chars)
  }
}
