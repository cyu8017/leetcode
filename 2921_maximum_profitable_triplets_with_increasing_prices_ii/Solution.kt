// LeetCode 2921 - Maximum Profitable Triplets With Increasing Prices II
// https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-ii/


class Solution {
    private lateinit var bit: IntArray

    fun maxProfit(prices: IntArray, profits: IntArray): Int {
        val n = prices.size
        var ans = -1
        val maxLeft = IntArray(n)
        bit = IntArray(5002)
        for (j in 0 until n) {
            maxLeft[j] = query(prices[j] - 1)
            update(prices[j], profits[j])
        }
        for (j in 0 until n) {
            var bestR = -1
            for (k in j + 1 until n) if (prices[k] > prices[j] && profits[k] > bestR) bestR = profits[k]
            if (maxLeft[j] >= 0 && bestR >= 0) {
                val cand = maxLeft[j] + profits[j] + bestR
                if (cand > ans) ans = cand
            }
        }
        return ans
    }

    private fun update(i0: Int, `val`: Int) {
        var i = i0
        while (i < bit.size) {
            if (`val` > bit[i]) bit[i] = `val`
            i += i and -i
        }
    }

    private fun query(i0: Int): Int {
        var i = i0
        var best = -1
        while (i > 0) {
            if (bit[i] > best) best = bit[i]
            i -= i and -i
        }
        return best
    }
}
