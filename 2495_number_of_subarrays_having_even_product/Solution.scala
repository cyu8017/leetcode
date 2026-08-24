// LeetCode 2495 - Number of Subarrays Having Even Product
// https://leetcode.com/problems/number-of-subarrays-having-even-product/

object Solution {
  def evenProduct(nums: Array[Int]): Long = {
    val n = nums.length.toLong
    val total = n * (n + 1) / 2
    var oddLen = 0L
    var odd = 0L
    var i = 0
    while (i < nums.length) {
      if (nums(i) % 2 == 1) {
        odd += 1
        oddLen += odd
      } else {
        odd = 0
      }
      i += 1
    }
    total - oddLen
  }
}
