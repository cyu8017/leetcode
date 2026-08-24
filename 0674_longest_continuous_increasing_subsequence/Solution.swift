// LeetCode 0674 - Longest Continuous Increasing Subsequence
// https://leetcode.com/problems/longest-continuous-increasing-subsequence/

class Solution {
    func findLengthOfLCIS(_ nums: [Int]) -> Int {
        var best = 1, cur = 1
        for i in 1..<nums.count {
            if nums[i] > nums[i - 1] {
                cur += 1
                best = max(best, cur)
            } else {
                cur = 1
            }
        }
        return best
    }
}
