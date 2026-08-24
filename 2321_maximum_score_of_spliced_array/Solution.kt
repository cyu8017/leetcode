// LeetCode 2321 - Maximum Score Of Spliced Array
// https://leetcode.com/problems/maximum-score-of-spliced-array/

class Solution {
    fun maximumsSplicedArray(nums1: IntArray, nums2: IntArray): Int {
        return maxOf(kadane(nums1, nums2), kadane(nums2, nums1))
    }

    private fun kadane(a: IntArray, b: IntArray): Int {
        var best = 0
        var cur = 0
        var sum = 0
        for (i in a.indices) {
            sum += a[i]
            cur += b[i] - a[i]
            if (cur < 0) cur = 0
            best = maxOf(best, cur)
        }
        return sum + best
    }
}
