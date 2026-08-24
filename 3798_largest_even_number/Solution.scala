// LeetCode 3798 - Largest Even Number
// https://leetcode.com/problems/largest-even-number/

object Solution {
  def largestEven(s0: String): String = {
    var s = s0
    while (s.length > 0 && s.charAt(s.length - 1) == '1') s = s.substring(0, s.length - 1)
    s
  }
}
