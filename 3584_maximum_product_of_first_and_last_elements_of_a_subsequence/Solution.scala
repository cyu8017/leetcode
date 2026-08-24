// LeetCode 3584 - Maximum Product of First and Last Elements of a Subsequence
// https://leetcode.com/problems/maximum-product-of-first-and-last-elements-of-a-subsequence/

object Solution {
  def maximumProduct(nums: Array[Int], m: Int): Long = {
    var ans = Long.MinValue
    var mx = Integer.MIN_VALUE
    var mi = Integer.MAX_VALUE
    var i = m - 1
    while (i < nums.length) {
      val x = nums(i)
      val y = nums(i - m + 1)
      mi = math.min(mi, y)
      mx = math.max(mx, y)
      ans = math.max(ans, math.max(1L * x * mi, 1L * x * mx))
      i += 1
    }
    ans
  }
}
