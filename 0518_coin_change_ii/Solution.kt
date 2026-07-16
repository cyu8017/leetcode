// LeetCode 0518 - Coin Change II
// https://leetcode.com/problems/coin-change-ii/

class Solution {
    fun change(amount: Int, coins: IntArray): Int {
        val dp = IntArray(amount + 1)
        dp[0] = 1
        for (coin in coins) {
            for (value in coin..amount) {
                dp[value] += dp[value - coin]
            }
        }
        return dp[amount]
    }
}
