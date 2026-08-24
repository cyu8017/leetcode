// LeetCode 2496 - Maximum Value of a String in an Array
// https://leetcode.com/problems/maximum-value-of-a-string-in-an-array/

object Solution {
  def maximumValue(strs: Array[String]): Int = {
    var ans = 0
    var si = 0
    while (si < strs.length) {
      val s = strs(si)
      var allDigit = true
      var value = 0
      var i = 0
      while (i < s.length && allDigit) {
        val c = s.charAt(i)
        if (c < '0' || c > '9') allDigit = false
        else value = value * 10 + (c - '0')
        i += 1
      }
      if (!allDigit) value = s.length
      if (value > ans) ans = value
      si += 1
    }
    ans
  }
}
