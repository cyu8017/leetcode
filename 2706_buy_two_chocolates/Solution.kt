// LeetCode 2706 - Buy Two Chocolates
// https://leetcode.com/problems/buy-two-chocolates/

class Solution {
    fun buyChoco(prices: IntArray, money: Int): Int {
        prices.sort()
        val cost = prices[0] + prices[1]
        return if (cost <= money) money - cost else money
    }
}
