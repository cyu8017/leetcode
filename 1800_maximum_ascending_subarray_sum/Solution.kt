// LeetCode 1800 - Maximum Ascending Subarray Sum
// https://leetcode.com/problems/maximum-ascending-subarray-sum/

class Solution {
    fun maxAscendingSum(nums: IntArray): Int {
        var best = nums[0]
        var cur = nums[0]
        for (i in 1 until nums.size) {
            cur = if (nums[i] > nums[i - 1]) cur + nums[i] else nums[i]
            best = maxOf(best, cur)
        }
        return best
    }
}
