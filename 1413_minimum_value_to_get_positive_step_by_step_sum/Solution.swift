// LeetCode 1413 - Minimum Value to Get Positive Step by Step Sum
// https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

class Solution {
    func minStartValue(_ nums: [Int]) -> Int {
        var prefix = 0, lowest = 0
        for value in nums {
            prefix += value
            lowest = min(lowest, prefix)
        }
        return 1 - lowest
    }
}
