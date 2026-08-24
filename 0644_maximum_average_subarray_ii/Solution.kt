// LeetCode 0644 - Maximum Average Subarray II
// https://leetcode.com/problems/maximum-average-subarray-ii/


class Solution {
    fun findMaxAverage(nums: IntArray, k: Int): Double {
        var left = nums.minOrNull()!!.toDouble()
        var right = nums.maxOrNull()!!.toDouble()
        while (right - left > 1e-5) {
            val mid = (left + right) / 2
            if (can(nums, k, mid)) left = mid else right = mid
        }
        return left
    }

    private fun can(nums: IntArray, k: Int, avg: Double): Boolean {
        var sum = 0.0
        for (i in 0 until k) sum += nums[i] - avg
        if (sum >= 0) return true
        var prefix = 0.0
        var minPrefix = 0.0
        for (i in k until nums.size) {
            sum += nums[i] - avg
            prefix += nums[i - k] - avg
            minPrefix = minOf(minPrefix, prefix)
            if (sum - minPrefix >= 0) return true
        }
        return false
    }
}
