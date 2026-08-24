// LeetCode 0718 - Maximum Length of Repeated Subarray
// https://leetcode.com/problems/maximum-length-of-repeated-subarray/

class Solution {
    fun findLength(nums1: IntArray, nums2: IntArray): Int {
        var m = nums1.size
        var n = nums2.size
        var best = 0
        var dp = IntArray(n + 1)
        for (i in 1 ..m) {
            var next = IntArray(n + 1)
            for (j in 1 ..n) {
                if (nums1[i - 1] == nums2[j - 1]) {
                    next[j] = dp[j - 1] + 1
                    best = maxOf(best, next[j])
                }
            }
            dp = next
        }
        return best
    }
}
