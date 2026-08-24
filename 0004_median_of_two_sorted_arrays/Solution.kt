// LeetCode 0004 - Median of Two Sorted Arrays
// https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution {
    fun findMedianSortedArrays(nums1: IntArray, nums2: IntArray): Double {
        var a = nums1
        var b = nums2
        if (a.size > b.size) {
            val tmp = a
            a = b
            b = tmp
        }

        val m = a.size
        val n = b.size
        val totalLeft = (m + n + 1) / 2
        var lo = 0
        var hi = m

        while (lo <= hi) {
            val i = (lo + hi) / 2
            val j = totalLeft - i

            val nums1LeftMax = if (i == 0) Int.MIN_VALUE else a[i - 1]
            val nums1RightMin = if (i == m) Int.MAX_VALUE else a[i]
            val nums2LeftMax = if (j == 0) Int.MIN_VALUE else b[j - 1]
            val nums2RightMin = if (j == n) Int.MAX_VALUE else b[j]

            if (nums1LeftMax <= nums2RightMin && nums2LeftMax <= nums1RightMin) {
                return if ((m + n) % 2 == 1) {
                    maxOf(nums1LeftMax, nums2LeftMax).toDouble()
                } else {
                    (maxOf(nums1LeftMax, nums2LeftMax) + minOf(nums1RightMin, nums2RightMin)) / 2.0
                }
            }

            if (nums1LeftMax > nums2RightMin) {
                hi = i - 1
            } else {
                lo = i + 1
            }
        }

        return 0.0
    }
}
