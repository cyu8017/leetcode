// LeetCode 3573 - Best Time to Buy and Sell Stock V
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-v/

class Solution {
    fun maximumProfit(prices: IntArray, k: Int): Long {
        val n = prices.size
        val f = Array(n) { Array(k + 1) { LongArray(3) } }
        for (j in 1..k) {
            f[0][j][1] = -prices[0].toLong()
            f[0][j][2] = prices[0].toLong()
        }
        for (i in 1 until n) {
            for (j in 1..k) {
                f[i][j][0] = maxOf(f[i - 1][j][0], maxOf(f[i - 1][j][1] + prices[i], f[i - 1][j][2] - prices[i]))
                f[i][j][1] = maxOf(f[i - 1][j][1], f[i - 1][j - 1][0] - prices[i])
                f[i][j][2] = maxOf(f[i - 1][j][2], f[i - 1][j - 1][0] + prices[i])
            }
        }
        return f[n - 1][k][0]
    }
}
