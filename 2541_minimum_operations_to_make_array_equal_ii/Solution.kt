// LeetCode 2541 - Minimum Operations to Make Array Equal II
// https://leetcode.com/problems/minimum-operations-to-make-array-equal-ii/

class Solution {
    fun minOperations(nums1: IntArray, nums2: IntArray, k: Int): Long {
        if (k == 0) {
            for (i in nums1.indices) {
                if (nums1[i] != nums2[i]) return -1
            }
            return 0
        }
        var pos = 0L
        var neg = 0L
        for (i in nums1.indices) {
            val d = nums1[i] - nums2[i]
            if (d % k != 0) return -1
            if (d > 0) pos += d / k
            else neg += (-d) / k
        }
        return if (pos != neg) -1 else pos
    }
}
