// LeetCode 3473 - Sum of K Subarrays With Length at Least M
// https://leetcode.com/problems/sum-of-k-subarrays-with-length-at-least-m/

class Solution {
    fun maxSum(nums: IntArray, k: Int, m: Int): Long {
        var n = nums.size
        var pref = LongArray(n + 1)
        for (i in 0 until n) { pref[i + 1] = pref[i] + nums[i] }
        val neg = -(1L  shl  60)
        var dp = Array(k + 1) { LongArray(n + 1) }
        for (t in 0 .. k) { dp[t].fill(neg) }
        for (i in 0 .. n) { dp[0][i] = 0 }
        for (t in 1 .. k) {
            var best = neg
            for (i in t * m .. n) {
                var j = i - m
                best = maxOf(best, dp[t - 1][j] - pref[j])
                dp[t][i] = best + pref[i]
            }
            for (i in 1 .. n) { dp[t][i] = maxOf(dp[t][i], dp[t][i - 1]) }
        }
        return dp[k][n]
    }
}
