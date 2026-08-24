// LeetCode 2771 - Longest Non-decreasing Subarray From Two Arrays
// https://leetcode.com/problems/longest-non-decreasing-subarray-from-two-arrays/

class Solution {
    fun maxNonDecreasingLength(nums1: IntArray, nums2: IntArray): Int {
        var n = nums1.size
        var dp1 = 1
        var dp2 = 1
        var ans = 1
        for (i in 1 until n) {
            var nd1 = 1
            var nd2 = 1
            if (nums1[i] >= nums1[i - 1]) nd1 = maxOf(nd1, dp1 + 1)
            if (nums1[i] >= nums2[i - 1]) nd1 = maxOf(nd1, dp2 + 1)
            if (nums2[i] >= nums1[i - 1]) nd2 = maxOf(nd2, dp1 + 1)
            if (nums2[i] >= nums2[i - 1]) nd2 = maxOf(nd2, dp2 + 1)
            dp1 = nd1
            dp2 = nd2
            ans = maxOf(ans, maxOf(dp1, dp2))
        }
        return ans
    }
}
