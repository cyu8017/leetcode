// LeetCode 1537 - Get the Maximum Score
// https://leetcode.com/problems/get-the-maximum-score/

class Solution {
    fun maxSum(nums1: IntArray, nums2: IntArray): Int {
        val mod = 1_000_000_007
        var i = 0
        var j = 0
        var first = 0L
        var second = 0L
        while (i < nums1.size || j < nums2.size) {
            when {
                j == nums2.size || (i < nums1.size && nums1[i] < nums2[j]) -> {
                    first += nums1[i]
                    i++
                }
                i == nums1.size || nums2[j] < nums1[i] -> {
                    second += nums2[j]
                    j++
                }
                else -> {
                    val best = maxOf(first, second) + nums1[i]
                    first = best
                    second = best
                    i++
                    j++
                }
            }
        }
        return (maxOf(first, second) % mod).toInt()
    }
}
