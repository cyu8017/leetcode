// LeetCode 0557 - Reverse Words in a String III
// https://leetcode.com/problems/reverse-words-in-a-string-iii/

object Solution {
  def reverseWords(s: String): String = {
    val chars = s.toCharArray
    val n = chars.length
    var start = 0
    var i = 0
    while (i <= n) {
      if (i == n || chars(i) == ' ') {
        reverse(chars, start, i - 1)
        start = i + 1
      }
      i += 1
    }
    new String(chars)
  }

  private def reverse(chars: Array[Char], left0: Int, right0: Int): Unit = {
    var left = left0
    var right = right0
    while (left < right) {
      val tmp = chars(left)
      chars(left) = chars(right)
      chars(right) = tmp
      left += 1
      right -= 1
    }
  }
}
