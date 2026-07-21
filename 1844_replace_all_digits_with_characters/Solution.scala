// LeetCode 1844 - Replace All Digits with Characters
// https://leetcode.com/problems/replace-all-digits-with-characters/

object Solution {
  def replaceDigits(s: String): String = {
    val chars = s.toArray
    var i = 1
    while (i < chars.length) {
      chars(i) = (chars(i - 1) + (chars(i) - '0')).toChar
      i += 2
    }
    new String(chars)
  }
}
