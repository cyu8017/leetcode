// LeetCode 2464 - Minimum Subarrays in a Valid Split
// https://leetcode.com/problems/minimum-subarrays-in-a-valid-split/

class Solution {
    fun validSubarraySplit(nums: IntArray): Int {
        val n = nums.size
        val INF = 1 shl 30
        val dp = IntArray(n + 1) { INF }
        dp[0] = 0
        for (i in 0 until n) {
            if (dp[i] >= INF) continue
            for (j in i until n) {
                if (gcd(nums[i], nums[j]) > 1) {
                    if (dp[i] + 1 < dp[j + 1]) dp[j + 1] = dp[i] + 1
                }
            }
        }
        return if (dp[n] >= INF) -1 else dp[n]
    }

    private fun gcd(a0: Int, b0: Int): Int {
        var a = a0
        var b = b0
        while (b != 0) {
            val t = a % b
            a = b
            b = t
        }
        return a
    }
}
