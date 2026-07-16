// LeetCode 0053 - Maximum Subarray
// https://leetcode.com/problems/maximum-subarray/

object Solution {
  def maxSubArray(nums: Array[Int]): Int = {
    var best = nums(0)
    var current = nums(0)

    var i = 1
    while (i < nums.length) {
      current = math.max(nums(i), current + nums(i))
      best = math.max(best, current)
      i += 1
    }

    best
  }
}
