// LeetCode 1736 - Latest Time by Replacing Hidden Digits
// https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/

object Solution {
  def maximumTime(time: String): String = {
    val chars = time.toCharArray
    if (chars(0) == '?') {
      chars(0) = if ("0123?".contains(chars(1))) '2' else '1'
    }
    if (chars(1) == '?') {
      chars(1) = if (chars(0) == '2') '3' else '9'
    }
    if (chars(3) == '?') {
      chars(3) = '5'
    }
    if (chars(4) == '?') {
      chars(4) = '9'
    }
    new String(chars)
  }
}
