// LeetCode 3349 - Adjacent Increasing Subarrays Detection I
// https://leetcode.com/problems/adjacent-increasing-subarrays-detection-i/

class Solution {
    fun hasIncreasingSubarrays(nums: MutableList<Int>, k: Int): Boolean {
        var n = nums.size
        var i = 0
        while (i + 2 * k <= n) {
            if (inc(nums, i, k) && inc(nums, i + k, k)) return true
            i++
        }
        return false
    }

    private fun inc(nums: MutableList<Int>, start: Int, k: Int): Boolean {
        var i = start
        while (i + 1 < start + k) {
            if (nums[i] >= nums[i + 1]) return false
            i++
        }
        return true
    }
}
