// LeetCode 0007 - Reverse Integer
// https://leetcode.com/problems/reverse-integer/

object Solution {
  def reverse(x: Int): Int = {
    var value = x
    var result = 0

    while (value != 0) {
      val pop = value % 10
      value /= 10

      if (result > Int.MaxValue / 10 || (result == Int.MaxValue / 10 && pop > 7)) {
        return 0
      }
      if (result < Int.MinValue / 10 || (result == Int.MinValue / 10 && pop < -8)) {
        return 0
      }

      result = result * 10 + pop
    }

    result
  }
}
