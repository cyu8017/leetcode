// LeetCode 2291 - Maximum Profit From Trading Stocks
// https://leetcode.com/problems/maximum-profit-from-trading-stocks/

class Solution {

    fun maximumProfit(present: IntArray, future: IntArray, budget: Int): Int {

            var n = present.size
            var dp = IntArray(budget + 1)
            for (i in 0 until n) {
                var profit = future[i] - present[i]
                if (profit <= 0) continue
                var cost = present[i]
                for (b in budget downTo cost) { dp[b] = maxOf(dp[b], dp[b - cost] + profit) }
            }
            return dp[budget]

    }

}
