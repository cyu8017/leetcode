// LeetCode 3105 - Longest Strictly Increasing or Strictly Decreasing Subarray
// https://leetcode.com/problems/longest-strictly-increasing-or-strictly-decreasing-subarray/

class Solution {
    func longestMonotonicSubarray(_ nums: [Int]) -> Int {
        var ans = 1, t = 1
        for i in 1..<nums.count {
            if nums[i - 1] < nums[i] {
                t += 1
                ans = max(ans, t)
            } else {
                t = 1
            }
        }
        t = 1
        for i in 1..<nums.count {
            if nums[i - 1] > nums[i] {
                t += 1
                ans = max(ans, t)
            } else {
                t = 1
            }
        }
        return ans
    }
}
