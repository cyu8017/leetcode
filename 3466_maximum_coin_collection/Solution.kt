// LeetCode 3466 - Maximum Coin Collection
// https://leetcode.com/problems/maximum-coin-collection/

class Solution {
    fun maxCoins(lane1: IntArray, lane2: IntArray): Long {
        val n = lane1.size
        val neg = -(1L shl 60)
        var dp = Array(2) { LongArray(2) }
        dp[0][0] = lane1[0].toLong()
        dp[1][0] = lane2[0].toLong()
        dp[0][1] = neg
        dp[1][1] = neg
        var ans = maxOf(dp[0][0], dp[1][0])
        for (i in 1 until n) {
            val ndp = Array(2) { LongArray(2) { neg } }
            ndp[0][0] = maxOf(dp[0][0], 0L) + lane1[i]
            ndp[1][0] = maxOf(dp[1][0], 0L) + lane2[i]
            ndp[0][1] = maxOf(dp[0][1], dp[1][0]) + lane1[i]
            ndp[1][1] = maxOf(dp[1][1], dp[0][0]) + lane2[i]
            if (lane1[i] > ndp[0][0]) ndp[0][0] = lane1[i].toLong()
            if (lane2[i] > ndp[1][0]) ndp[1][0] = lane2[i].toLong()
            for (a in 0 until 2) for (b in 0 until 2) if (ndp[a][b] > ans) ans = ndp[a][b]
            dp = ndp
        }
        return ans
    }
}
