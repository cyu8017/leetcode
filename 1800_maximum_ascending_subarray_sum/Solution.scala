// LeetCode 1800 - Maximum Ascending Subarray Sum
// https://leetcode.com/problems/maximum-ascending-subarray-sum/

object Solution {
  def maxAscendingSum(nums: Array[Int]): Int = {
    var best = nums(0)
    var cur = nums(0)
    for (i <- 1 until nums.length) {
      cur = if (nums(i) > nums(i - 1)) cur + nums(i) else nums(i)
      best = math.max(best, cur)
    }
    best
  }
}
