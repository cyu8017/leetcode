// LeetCode 2944 - Minimum Number of Coins for Fruits
// https://leetcode.com/problems/minimum-number-of-coins-for-fruits/

class Solution {
    fun minimumCoins(prices: IntArray): Int {
        val n = prices.size
        val dp = IntArray(n + 1) { 1 shl 30 }
        dp[0] = 0
        for (i in 1..n) {
            var j = i
            while (j <= n && j <= i + i) {
                val cand = dp[i - 1] + prices[i - 1]
                if (cand < dp[j]) dp[j] = cand
                j++
            }
        }
        return dp[n]
    }
}
