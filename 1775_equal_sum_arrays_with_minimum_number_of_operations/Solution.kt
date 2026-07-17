// LeetCode 1775 - Equal Sum Arrays With Minimum Number of Operations
// https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/

class Solution {
    fun minOperations(nums1: IntArray, nums2: IntArray): Int {
        if (nums1.size * 6 < nums2.size || nums2.size * 6 < nums1.size) {
            return -1
        }
        var s1 = nums1.sum()
        var s2 = nums2.sum()
        if (s1 == s2) {
            return 0
        }
        var big = nums1
        var small = nums2
        if (s1 < s2) {
            big = nums2
            small = nums1
            val tmp = s1
            s1 = s2
            s2 = tmp
        }
        var diff = s1 - s2
        val gains = IntArray(big.size + small.size)
        var k = 0
        for (x in big) {
            gains[k++] = x - 1
        }
        for (x in small) {
            gains[k++] = 6 - x
        }
        gains.sortDescending()
        var ops = 0
        for (gain in gains) {
            if (diff <= 0) {
                break
            }
            diff -= gain
            ops++
        }
        return if (diff <= 0) ops else -1
    }
}
