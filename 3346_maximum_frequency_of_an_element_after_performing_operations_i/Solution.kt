// LeetCode 3346 - Maximum Frequency of an Element After Performing Operations I
// https://leetcode.com/problems/maximum-frequency-of-an-element-after-performing-operations-i/

class Solution {
    fun maxFrequency(nums: IntArray, k: Int, numOperations: Int): Int {
        nums.sort()
        val n = nums.size
        val freq = HashMap<Int, Int>()
        for (x in nums) freq[x] = (freq[x] ?: 0) + 1
        var ans = 1
        for ((t, f) in freq) {
            val lo = lowerBound(nums, t - k)
            val hi = upperBound(nums, t + k)
            val can = hi - lo
            val use = minOf(can, f + numOperations)
            if (use > ans) ans = use
        }
        var l = 0
        for (r in 0 until n) {
            while (nums[r] - nums[l] > 2 * k) l++
            val window = minOf(r - l + 1, numOperations)
            if (window > ans) ans = window
        }
        return ans
    }

    private fun lowerBound(a: IntArray, x: Int): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (a[mid] < x) lo = mid + 1 else hi = mid
        }
        return lo
    }

    private fun upperBound(a: IntArray, x: Int): Int {
        var lo = 0
        var hi = a.size
        while (lo < hi) {
            val mid = (lo + hi) / 2
            if (a[mid] <= x) lo = mid + 1 else hi = mid
        }
        return lo
    }
}
