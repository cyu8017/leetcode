// LeetCode 1838 - Frequency of the Most Frequent Element
// https://leetcode.com/problems/frequency-of-the-most-frequent-element/

class Solution {
    fun maxFrequency(nums: IntArray, k: Int): Int {
        nums.sort()
        var left = 0
        var windowSum = 0L
        var best = 0
        for (right in nums.indices) {
            val value = nums[right].toLong()
            windowSum += value
            while (value * (right - left + 1) - windowSum > k) {
                windowSum -= nums[left]
                left++
            }
            best = maxOf(best, right - left + 1)
        }
        return best
    }
}
