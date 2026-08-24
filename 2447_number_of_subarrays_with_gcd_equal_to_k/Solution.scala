// LeetCode 2447 - Number of Subarrays With GCD Equal to K
// https://leetcode.com/problems/number-of-subarrays-with-gcd-equal-to-k/

object Solution {
  def subarrayGCD(nums: Array[Int], k: Int): Int = {
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
    var ans = 0
    val n = nums.length
    var i = 0
    while (i < n) {
      var g = 0
      var j = i
      while (j < n) {
        g = gcd(g, nums(j))
        if (g < k) j = n
        else {
          if (g == k) ans += 1
          j += 1
        }
      }
      i += 1
    }
    ans
  }
}
