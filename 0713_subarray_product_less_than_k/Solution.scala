// LeetCode 0713 - Subarray Product Less Than K
// https://leetcode.com/problems/subarray-product-less-than-k/

object Solution {
  def numSubarrayProductLessThanK(nums: Array[Int], k: Int): Int = {
    if (k <= 1) return 0
    var product = 1L
    var left = 0
    var ans = 0
    var right = 0
    while (right < nums.length) {
      product *= nums(right)
      while (product >= k) {
        product /= nums(left)
        left += 1
      }
      ans += right - left + 1
      right += 1
    }
    ans
  }
}
