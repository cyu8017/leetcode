// LeetCode 1749 - Maximum Absolute Sum of Any Subarray
// https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

object Solution {
  def maxAbsoluteSum(nums: Array[Int]): Int = {
    var prefix = 0
    var low = 0
    var high = 0
    for (value <- nums) {
      prefix += value
      low = math.min(low, prefix)
      high = math.max(high, prefix)
    }
    high - low
  }
}
