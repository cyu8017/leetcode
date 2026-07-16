// LeetCode 0541 - Reverse String II
// https://leetcode.com/problems/reverse-string-ii/

object Solution {
  def reverseStr(s: String, k: Int): String = {
    val chars = s.toCharArray
    var start = 0
    while (start < chars.length) {
      var left = start
      var right = math.min(start + k, chars.length) - 1
      while (left < right) {
        val temp = chars(left)
        chars(left) = chars(right)
        chars(right) = temp
        left += 1
        right -= 1
      }
      start += 2 * k
    }
    new String(chars)
  }
}
