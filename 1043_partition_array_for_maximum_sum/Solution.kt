// LeetCode 1043 - Partition Array for Maximum Sum
// https://leetcode.com/problems/partition-array-for-maximum-sum/

class Solution {
    fun maxSumAfterPartitioning(arr: IntArray, k: Int): Int {
        val n = arr.size
        val dp = IntArray(n + 1)
        for (i in 1..n) {
            var best = 0
            val limit = minOf(k, i)
            for (size in 1..limit) {
                best = maxOf(best, arr[i - size])
                dp[i] = maxOf(dp[i], dp[i - size] + best * size)
            }
        }
        return dp[n]
    }
}
