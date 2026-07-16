// LeetCode 0053 - Maximum Subarray
// https://leetcode.com/problems/maximum-subarray/

class Solution {
    fun maxSubArray(nums: IntArray): Int {
        var best = nums[0]
        var current = nums[0]

        for (i in 1 until nums.size) {
            current = maxOf(nums[i], current + nums[i])
            best = maxOf(best, current)
        }

        return best
    }
}
