// LeetCode 1800 - Maximum Ascending Subarray Sum
// https://leetcode.com/problems/maximum-ascending-subarray-sum/

class Solution {
    func maxAscendingSum(_ nums: [Int]) -> Int {
        var best = nums[0]
        var cur = nums[0]
        for i in 1..<nums.count {
            if nums[i] > nums[i - 1] {
                cur += nums[i]
            } else {
                cur = nums[i]
            }
            best = max(best, cur)
        }
        return best
    }
}
