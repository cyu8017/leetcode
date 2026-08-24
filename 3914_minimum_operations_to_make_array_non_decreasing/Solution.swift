// LeetCode 3914 - Minimum Operations To Make Array Non Decreasing
// https://leetcode.com/problems/minimum-operations-to-make-array-non-decreasing/

class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var ans = 0
        if nums.count > 1 {
            for i in 1..<nums.count {
                ans += max(0, nums[i - 1] - nums[i])
            }
        }
        return ans
    }
}
