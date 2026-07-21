// LeetCode 1827 - Minimum Operations to Make the Array Increasing
// https://leetcode.com/problems/minimum-operations-to-make-the-array-increasing/

class Solution {
    fun minOperations(nums: IntArray): Int {
        var ops = 0
        var prev = nums[0]
        for (i in 1 until nums.size) {
            val value = nums[i]
            if (value <= prev) {
                val needed = prev + 1
                ops += needed - value
                prev = needed
            } else {
                prev = value
            }
        }
        return ops
    }
}
