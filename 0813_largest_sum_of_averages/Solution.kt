// LeetCode 0813 - Largest Sum of Averages
// https://leetcode.com/problems/largest-sum-of-averages/

class Solution {
    fun largestSumOfAverages(nums: IntArray, k: Int): Double {
        var n = nums.size
        var prefix = DoubleArray(n + 1)
        for (i in 0 until n) { prefix[i + 1] = prefix[i] + nums[i] }
        var dp = DoubleArray(n)
        for (i in 0 until n) { dp[i] = (prefix[i + 1] - prefix[0]) / (i + 1) }
        for (groups in 2 until = k) {
            var nxt = DoubleArray(n)
            for (i in groups - 1 until n) {
                var best = 0.0
                for (j in groups - 2 until i) {
                    best = maxOf(best, dp[j] + (prefix[i + 1] - prefix[j + 1]) / (i - j))
                }
                nxt[i] = best
            }
            dp = nxt
        }
        return dp[n - 1]
    }
}
