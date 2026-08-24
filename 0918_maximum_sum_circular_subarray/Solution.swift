// LeetCode 0918 - Maximum Sum Circular Subarray
// https://leetcode.com/problems/maximum-sum-circular-subarray/

class Solution {
    func maxSubarraySumCircular(_ nums: [Int]) -> Int {
        let total = nums.reduce(0, +)
        var maxSum = nums[0], minSum = nums[0], curMax = nums[0], curMin = nums[0]
        for i in 1..<nums.count {
            curMax = max(nums[i], curMax + nums[i])
            curMin = min(nums[i], curMin + nums[i])
            maxSum = max(maxSum, curMax)
            minSum = min(minSum, curMin)
        }
        if maxSum < 0 { return maxSum }
        return max(maxSum, total - minSum)
    }
}
