// LeetCode 3132 - Find the Integer Added to Array II
// https://leetcode.com/problems/find-the-integer-added-to-array-ii/

class Solution {
    fun minimumAddedInteger(nums1: IntArray, nums2: IntArray): Int {
        nums1.sort()
        nums2.sort()
        var ans = 1  shl  30
        for (t in 0 until 3) {
            var x = nums2[0] - nums1[t]
            if (ok(nums1, nums2, x)) ans = minOf(ans, x)
        }
        return ans
    }

    private fun ok(nums1: IntArray, nums2: IntArray, x: Int): Boolean {
        var i = 0
        var j = 0
        var cnt = 0
        while (i < nums1.size && j < nums2.size) {
            if (nums2[j] - nums1[i] != x) cnt++
            else j++
            i++
        }
        return cnt <= 2
    }
}
