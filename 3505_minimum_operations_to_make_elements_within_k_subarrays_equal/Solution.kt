// LeetCode 3505 - Minimum Operations to Make Elements Within K Subarrays Equal
// https://leetcode.com/problems/minimum-operations-to-make-elements-within-k-subarrays-equal/

class Solution {
    fun minOperations(nums: IntArray, x: Int, k: Int): Long {
        val n = nums.size
        val minOps = LongArray(n - x + 1)
        for (i in 0..n - x) {
            val w = nums.copyOfRange(i, i + x)
            w.sort()
            val med = w[(x - 1) / 2]
            var ops = 0L
            for (v in w) ops += kotlin.math.abs(v - med).toLong()
            minOps[i] = ops
        }
        val Inf = 1L shl 62
        val dp = Array(n + 1) { LongArray(k + 1) { Inf } }
        dp[n][0] = 0
        for (i in n - 1 downTo 0) {
            for (j in 0..k) {
                dp[i][j] = dp[i + 1][j]
                if (j > 0 && i + x <= n && minOps[i] + dp[i + x][j - 1] < dp[i][j]) {
                    dp[i][j] = minOps[i] + dp[i + x][j - 1]
                }
            }
        }
        return dp[0][k]
    }
}
