// LeetCode 2864 - Maximum Odd Binary Number
// https://leetcode.com/problems/maximum-odd-binary-number/

object Solution {
  def maximumOddBinaryNumber(s: String): String = {
    val ones = s.count(_ == '1')
    val zeros = s.length - ones
    "1" * (ones - 1) + "0" * zeros + "1"
  }
}
