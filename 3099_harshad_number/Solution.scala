// LeetCode 3099 - Harshad Number
// https://leetcode.com/problems/harshad-number/

object Solution {
  def sumOfTheDigitsOfHarshadNumber(x: Int): Int = {
    var s = 0
    var y = x
    while (y > 0) {
      s += y % 10
      y /= 10
    }
    if (x % s == 0) s else -1
  }
}
