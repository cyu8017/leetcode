// LeetCode 0209 - Minimum Size Subarray Sum
// https://leetcode.com/problems/minimum-size-subarray-sum/

class Solution {
    func minSubArrayLen(_ target: Int, _ nums: [Int]) -> Int {
        var left = 0
        var sum = 0
        var best = Int.max
        for right in nums.indices {
            sum += nums[right]
            while sum >= target {
                best = min(best, right - left + 1)
                sum -= nums[left]
                left += 1
            }
        }
        return best == Int.max ? 0 : best
    }
}