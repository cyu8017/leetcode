// LeetCode 2540 - Minimum Common Value
// https://leetcode.com/problems/minimum-common-value/

class Solution {
    fun getCommon(nums1: IntArray, nums2: IntArray): Int {
        var i = 0
        var j = 0
        while (i < nums1.size && j < nums2.size) {
            if (nums1[i] == nums2[j]) return nums1[i]
            if (nums1[i] < nums2[j]) { i = i + 1 }
            else { j = j + 1 }
        }
        return -1
    }
}
