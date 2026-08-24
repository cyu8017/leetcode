// LeetCode 2918 - Minimum Equal Sum of Two Arrays After Replacing Zeros
// https://leetcode.com/problems/minimum-equal-sum-of-two-arrays-after-replacing-zeros/

class Solution {
    fun minSum(nums1: IntArray, nums2: IntArray): Long {
        var s1 = 0
        var s2 = 0
        var z1 = 0
        var z2 = 0
        for (v in nums1) {
            if (v == 0) {
                z1++
                s1++
            } else s1 += v
        }
        for (v in nums2) {
            if (v == 0) {
                z2++
                s2++
            } else s2 += v
        }
        if (z1 == 0 && s1 < s2) return -1
        if (z2 == 0 && s2 < s1) return -1
        return if (s1 > s2) s1 else s2
    }
}
