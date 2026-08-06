// LeetCode 1903 - Largest Odd Number in String
// https://leetcode.com/problems/largest-odd-number-in-string/

object Solution {
  def largestOddNumber(num: String): String = {
    var i = num.length - 1
    while (i >= 0) {
      if ((num.charAt(i) - '0') % 2 == 1) return num.substring(0, i + 1)
      i -= 1
    }
    ""
  }
}
