// LeetCode 2969 - Minimum Number of Coins for Fruits II
// https://leetcode.com/problems/minimum-number-of-coins-for-fruits-ii/

class Solution {
    fun minimumCoins(prices: IntArray): Int {
        var n = prices.size
        var dp = IntArray(n + 1)
        for (i in 0..n) { dp[i] = 1 shl 30 }
        dp[0] = 0
        for (i in 1..n) {
            for (j in i..n && j <= 2 * i) {
                dp[j] = minOf(dp[j], dp[i - 1] + prices[i - 1])
            }
        }
        return dp[n]
    }
}
