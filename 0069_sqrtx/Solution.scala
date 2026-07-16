// LeetCode 0069 - Sqrt(x)
// https://leetcode.com/problems/sqrtx/

object Solution {
  def mySqrt(x: Int): Int = {
    if (x < 2) {
      return x
    }

    var left = 2
    var right = x / 2

    while (left <= right) {
      val mid = left + (right - left) / 2
      val square = mid.toLong * mid
      if (square == x.toLong) {
        return mid
      }
      if (square < x) {
        left = mid + 1
      } else {
        right = mid - 1
      }
    }

    right
  }
}
