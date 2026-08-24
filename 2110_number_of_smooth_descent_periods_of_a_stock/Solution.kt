// LeetCode 2110 - Number of Smooth Descent Periods of a Stock
// https://leetcode.com/problems/number-of-smooth-descent-periods-of-a-stock/

class Solution {
    fun getDescentPeriods(prices: IntArray): Long {
        var ans: Long = 1, cur = 1
        for (i in 1 until prices.size) {
            if (prices[i] == prices[i - 1] - 1) cur++
            else cur = 1
            ans += cur
        }
        return ans
    }
}
