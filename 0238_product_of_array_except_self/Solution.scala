// LeetCode 0238 - Product of Array Except Self
// https://leetcode.com/problems/product-of-array-except-self/

object Solution {
  def productExceptSelf(nums: Array[Int]): Array[Int] = {
    val length = nums.length
    val result = Array.fill(length)(1)
    var prefix = 1
    for (index <- 0 until length) {
      result(index) = prefix
      prefix *= nums(index)
    }
    var suffix = 1
    for (index <- length - 1 to 0 by -1) {
      result(index) *= suffix
      suffix *= nums(index)
    }
    result
  }
}
