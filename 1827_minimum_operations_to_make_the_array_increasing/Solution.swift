// LeetCode 1827 - Minimum Operations to Make the Array Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

class Solution {
    func minOperations(_ nums: [Int]) -> Int {
        var ops = 0
        var prev = nums[0]
        for value in nums.dropFirst() {
            if value <= prev {
                let needed = prev + 1
                ops += needed - value
                prev = needed
            } else {
                prev = value
            }
        }
        return ops
    }
}
