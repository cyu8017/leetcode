// LeetCode 1413 - Minimum Value to Get Positive Step by Step Sum
// https://leetcode.com/problems/minimum-value-to-get-positive-step-by-step-sum/

class Solution {
    fun minStartValue(nums: IntArray): Int {
        var prefix = 0
        var lowest = 0
        for (value in nums) {
            prefix += value
            lowest = minOf(lowest, prefix)
        }
        return 1 - lowest
    }
}
