// LeetCode 3411 - Maximum Subarray With Equal Products
// https://leetcode.com/problems/maximum-subarray-with-equal-products/

object Solution {
  private def gcd(a0: Int, b0: Int): Int = {
    var a = a0
    var b = b0
    while (b != 0) {
      val t = a % b
      a = b
      b = t
    }
    a
  }

  def maxLength(nums: Array[Int]): Int = {
    val n = nums.length
    var ans = 1
    var i = 0
    while (i < n) {
      var prod = 1L
      var g = 0
      var l = 1
      var j = i
      var stop = false
      while (j < n && !stop) {
        if (prod > 1000000000L / nums(j)) stop = true
        else {
          prod *= nums(j)
          if (g == 0) {
            g = nums(j)
            l = nums(j)
          } else {
            g = gcd(g, nums(j))
            l = l / gcd(l, nums(j)) * nums(j)
          }
          if (prod == l.toLong * g && j - i + 1 > ans) ans = j - i + 1
          j += 1
        }
      }
      i += 1
    }
    ans
  }
}
