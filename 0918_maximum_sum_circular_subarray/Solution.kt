// LeetCode 0918 - Maximum Sum Circular Subarray
// https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution {
    fun maxSubarraySumCircular(nums: IntArray): Int {
        var total = 0
        for (x in nums) { total += x; }
        var maxSum = nums[0]
        var minSum = nums[0]
        var curMax = nums[0]
        var curMin = nums[0]
        for (i in 1 until nums.size) {
            curMax = maxOf(nums[i], curMax + nums[i])
            curMin = minOf(nums[i], curMin + nums[i])
            maxSum = maxOf(maxSum, curMax)
            minSum = minOf(minSum, curMin)
        }
        if (maxSum < 0) return maxSum
        return maxOf(maxSum, total - minSum)
    }
}
