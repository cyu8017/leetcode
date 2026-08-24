// LeetCode 3982 - Sum of Integers with Maximum Digit Range
// https://leetcode.com/problems/sum-of-integers-with-maximum-digit-range/

object Solution {
  def maxDigitRange(nums: Array[Int]): Int = {
    var mx = 0
    var ans = 0
    for (x <- nums) {
      var a = 10
      var b = 0
      var y = x
      while (y > 0) {
        val v = y % 10
        a = math.min(a, v)
        b = math.max(b, v)
        y /= 10
      }
      val r = b - a
      if (mx < r) {
        mx = r
        ans = x
      } else if (mx == r) ans += x
    }
    ans
  }
}
