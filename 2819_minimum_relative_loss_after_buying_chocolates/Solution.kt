// LeetCode 2819 - Minimum Relative Loss After Buying Chocolates
// https://leetcode.com/problems/minimum-relative-loss-after-buying-chocolates/

class Solution {
    fun minimumRelativeLosses(prices: IntArray, queries: Array<IntArray>): LongArray {
        prices.sort()
        var n = prices.size
        var ans = LongArray(queries.size)
        for (qi in 0 until queries.size) {
            var kk = queries[qi][0]
            var m = queries[qi][1]
            var losses = LongArray(n)
            for (i in 0 until n) {
                if (prices[i] <= kk) losses[i] = prices[i]
                else losses[i] = 2L * kk - prices[i]
            }
            losses.sort()
            var sum = 0
            for (i in 0 until m) { sum += losses[i] }
            ans[qi] = sum
        }
        return ans
    }
}
