// LeetCode 2934 - Minimum Operations to Maximize Last Elements in Arrays
// https://leetcode.com/problems/minimum-operations-to-maximize-last-elements-in-arrays/

class Solution {
    fun minOperations(nums1: IntArray, nums2: IntArray): Int {
        var n = nums1.size
        var ans = calc(nums1, nums2)
        var t = nums1[n - 1]
        nums1[n - 1] = nums2[n - 1]
        nums2[n - 1] = t
        var cand = calc(nums1, nums2) + 1
        if (cand < ans) ans = cand
        return ans >= if ((1  shl  30)) -1 else ans
    }

    private fun calc(a1: IntArray, a2: IntArray): Int {
        var n = a1.size
        var ops = 0
        var last1 = a1[n - 1]
        var last2 = a2[n - 1]
        for (i in 0 until n - 1) {
            var x = a1[i]
            var y = a2[i]
            if (x <= last1 && y <= last2) continue
            if (y <= last1 && x <= last2) {
                ops++
                continue
            }
            return 1  shl  30
        }
        return ops
    }
}
