// LeetCode 2436 - Minimum Split Into Subarrays With GCD Greater Than One
// https://leetcode.com/problems/minimum-split-into-subarrays-with-gcd-greater-than-one/

object Solution {
  def minimumSplits(nums: Array[Int]): Int = {
    def gcd(x: Int, y: Int): Int = {
      var a = x
      var b = y
      while (b != 0) {
        val t = a % b
        a = b
        b = t
      }
      a
    }
    var ans = 1
    var g = nums(0)
    var i = 1
    while (i < nums.length) {
      val ng = gcd(g, nums(i))
      if (ng == 1) {
        ans += 1
        g = nums(i)
      } else {
        g = ng
      }
      i += 1
    }
    ans
  }
}
