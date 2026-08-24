// LeetCode 2907 - Maximum Profitable Triplets With Increasing Prices I
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-i/


class Solution {
    fun maxProfit(prices: IntArray, profits: IntArray): Int {
        val n = prices.size
        var ans = -1
        for (j in 0 until n) {
            var bestL = -1
            var bestR = -1
            for (i in 0 until j) if (prices[i] < prices[j] && profits[i] > bestL) bestL = profits[i]
            for (k in j + 1 until n) if (prices[k] > prices[j] && profits[k] > bestR) bestR = profits[k]
            if (bestL >= 0 && bestR >= 0) {
                val cand = bestL + profits[j] + bestR
                if (cand > ans) ans = cand
            }
        }
        return ans
    }
}
