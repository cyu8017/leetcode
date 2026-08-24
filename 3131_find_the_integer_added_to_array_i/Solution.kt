// LeetCode 3131 - Find the Integer Added to Array I
// https://leetcode.com/problems/find-the-integer-added-to-array-i/

class Solution {
    fun addedInteger(nums1: IntArray, nums2: IntArray): Int {
        var min1 = nums1[0]
        var min2 = nums2[0]
        for (x in nums1) { min1 = minOf(min1, x) }
        for (x in nums2) { min2 = minOf(min2, x) }
        return min2 - min1
    }
}
