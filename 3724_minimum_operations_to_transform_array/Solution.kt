// LeetCode 3724 - Minimum Operations to Transform Array
// https://leetcode.com/problems/minimum-operations-to-transform-array/

class Solution {
    fun minOperations(nums1: IntArray, nums2: IntArray): Long {
        var ans = 1
        var n = nums1.size
        var ok = false
        var d = 1  shl  30
        for (i in 0 until n) {
            var x = maxOf(nums1[i], nums2[i])
            var y = minOf(nums1[i], nums2[i])
            ans += x - y
            d = minOf(d, minOf(kotlin.math.abs(x - nums2[n]), kotlin.math.abs(y - nums2[n])))
            if (nums2[n] >= y && nums2[n] <= x) ok = true
        }
        if (!ok) ans += d
        return ans
    }
}
