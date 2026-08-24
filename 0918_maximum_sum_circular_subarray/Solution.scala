// LeetCode 0918 - Maximum Sum Circular Subarray
// https://leetcode.com/problems/maximum-sum-circular-subarray/

object Solution {
  def maxSubarraySumCircular(nums: Array[Int]): Int = {
    var total = 0
    nums.foreach(x => total += x)
    var maxSum = nums(0)
    var minSum = nums(0)
    var curMax = nums(0)
    var curMin = nums(0)
    var i = 1
    while (i < nums.length) {
      curMax = math.max(nums(i), curMax + nums(i))
      curMin = math.min(nums(i), curMin + nums(i))
      maxSum = math.max(maxSum, curMax)
      minSum = math.min(minSum, curMin)
      i += 1
    }
    if (maxSum < 0) maxSum
    else math.max(maxSum, total - minSum)
  }
}
