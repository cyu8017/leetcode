// LeetCode 0801 - Minimum Swaps To Make Sequences Increasing
// https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/

class Solution {
    fun minSwap(nums1: IntArray, nums2: IntArray): Int {
        var n = nums1.size
        var swap = IntArray(n), keep = IntArray(n)
        java.util.swap.fill(n)
        java.util.keep.fill(n)
        swap[0] = 1
        keep[0] = 0
        for (i in 1 until n) {
            if (nums1[i] > nums1[i - 1] && nums2[i] > nums2[i - 1]) {
                keep[i] = keep[i - 1]
                swap[i] = swap[i - 1] + 1
            }
            if (nums1[i] > nums2[i - 1] && nums2[i] > nums1[i - 1]) {
                keep[i] = minOf(keep[i], swap[i - 1])
                swap[i] = minOf(swap[i], keep[i - 1] + 1)
            }
        }
        return minOf(swap[n - 1], keep[n - 1])
    }
}
