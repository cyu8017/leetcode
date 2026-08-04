// LeetCode 1458 - Max Dot Product of Two Subsequences
// https://leetcode.com/problems/max-dot-product-of-two-subsequences/

class Solution {
    fun maxDotProduct(nums1: IntArray, nums2: IntArray): Int {
        val n = nums2.size
        val dp = LongArray(n + 1) { Long.MIN_VALUE / 4 }
        for (a in nums1) {
            val prev = dp.copyOf()
            for (j in 1..n) {
                val product = a.toLong() * nums2[j - 1]
                dp[j] = maxOf(
                    dp[j - 1],
                    prev[j],
                    product,
                    product + maxOf(0L, prev[j - 1])
                )
            }
        }
        return dp[n].toInt()
    }
}
