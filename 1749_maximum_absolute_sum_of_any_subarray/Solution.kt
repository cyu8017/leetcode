// LeetCode 1749 - Maximum Absolute Sum of Any Subarray
// https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution {
    fun maxAbsoluteSum(nums: IntArray): Int {
        var prefix = 0
        var low = 0
        var high = 0
        for (value in nums) {
            prefix += value
            low = minOf(low, prefix)
            high = maxOf(high, prefix)
        }
        return high - low
    }
}
