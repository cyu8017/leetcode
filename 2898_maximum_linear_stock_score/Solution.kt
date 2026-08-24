// LeetCode 2898 - Maximum Linear Stock Score
// https://leetcode.com/problems/maximum-linear-stock-score/

class Solution {
    fun maxScore(prices: IntArray): Long {
        val best = HashMap<Int, Long>()
        var ans = 0L
        for (i in prices.indices) {
            val key = prices[i] - (i + 1)
            val cand = best.getOrDefault(key, 0L) + prices[i]
            if (cand > best.getOrDefault(key, 0L)) best[key] = cand
            if (best[key]!! > ans) ans = best[key]!!
        }
        return ans
    }
}
