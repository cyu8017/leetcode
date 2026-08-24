// LeetCode 3652 - Best Time to Buy and Sell Stock using Strategy
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/

class Solution {
    fun maxProfit(prices: IntArray, strategy: IntArray, k: Int): Long {
        val n = prices.size
        val s = LongArray(n + 1)
        val t = LongArray(n + 1)
        for (i in 1..n) {
            s[i] = s[i - 1] + 1L * prices[i - 1] * strategy[i - 1]
            t[i] = t[i - 1] + prices[i - 1]
        }
        var ans = s[n]
        for (i in k..n) {
            ans = maxOf(ans, s[n] - (s[i] - s[i - k]) + (t[i] - t[i - k / 2]))
        }
        return ans
    }
}
