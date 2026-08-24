// LeetCode 2443 - Sum of Number and Its Reverse
// https://leetcode.com/problems/sum-of-number-and-its-reverse/

object Solution {
  def sumOfNumberAndReverse(num: Int): Boolean = {
    def rev(x0: Int): Int = {
      var x = x0
      var r = 0
      while (x > 0) {
        r = r * 10 + x % 10
        x /= 10
      }
      r
    }
    var i = 0
    while (i <= num) {
      if (i + rev(i) == num) return true
      i += 1
    }
    false
  }
}
