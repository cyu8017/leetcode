// LeetCode 1475 - Final Prices With a Special Discount in a Shop
// https://leetcode.com/problems/final-prices-with-a-special-discount-in-a-shop/

class Solution {
    fun finalPrices(prices: IntArray): IntArray {
        val ans = prices.copyOf()
        val stack = ArrayDeque<Int>()
        for (i in prices.indices) {
            while (stack.isNotEmpty() && prices[stack.last()] >= prices[i]) {
                val j = stack.removeLast()
                ans[j] -= prices[i]
            }
            stack.add(i)
        }
        return ans
    }
}
