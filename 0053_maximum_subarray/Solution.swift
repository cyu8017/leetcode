// LeetCode 0053 - Maximum Subarray
// https://leetcode.com/problems/maximum-subarray/

class Solution {
    func maxSubArray(_ nums: [Int]) -> Int {
        var best = nums[0]
        var current = nums[0]

        for i in 1..<nums.count {
            current = max(nums[i], current + nums[i])
            best = max(best, current)
        }

        return best
    }
}
