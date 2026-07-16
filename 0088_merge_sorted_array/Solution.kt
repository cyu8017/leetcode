// LeetCode 0088 - Merge Sorted Array
// https://leetcode.com/problems/merge-sorted-array/

class Solution {
    fun merge(nums1: IntArray, m: Int, nums2: IntArray, n: Int) {
        var i = m - 1
        var j = n - 1
        var write = m + n - 1

        while (j >= 0) {
            if (i >= 0 && nums1[i] > nums2[j]) {
                nums1[write] = nums1[i]
                i--
            } else {
                nums1[write] = nums2[j]
                j--
            }
            write--
        }
    }
}
