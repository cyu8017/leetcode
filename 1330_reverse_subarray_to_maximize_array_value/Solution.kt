// LeetCode 1330 - Reverse Subarray To Maximize Array Value
// https://leetcode.com/problems/reverse-subarray-to-maximize-array-value/

class Solution {
    fun maxValueAfterReverse(nums: IntArray): Int {
        var base = 0
        for (i in 0 until nums.size - 1) base += kotlin.math.abs(nums[i] - nums[i + 1])
        var gain = 0
        var low = Int.MAX_VALUE
        var high = Int.MIN_VALUE
        for (i in 0 until nums.size - 1) {
            val a = nums[i]
            val b = nums[i + 1]
            gain = maxOf(
                gain,
                kotlin.math.abs(nums[0] - b) - kotlin.math.abs(a - b),
                kotlin.math.abs(nums[nums.size - 1] - a) - kotlin.math.abs(a - b)
            )
            low = minOf(low, maxOf(a, b))
            high = maxOf(high, minOf(a, b))
        }
        return base + maxOf(gain, 2 * (high - low))
    }
}
