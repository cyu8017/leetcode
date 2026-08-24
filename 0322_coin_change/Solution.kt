// LeetCode 0322 - Coin Change

// https://leetcode.com/problems/coin-change/



class Solution {

    fun coinChange(coins: IntArray, amount: Int): Int {

        val maxValue = amount + 1

        val dp = IntArray(amount + 1) { maxValue }

        dp[0] = 0

        for (coin in coins) {

            for (value in coin..amount) {

                dp[value] = minOf(dp[value], dp[value - coin] + 1)

            }

        }

        return if (dp[amount] == maxValue) -1 else dp[amount]

    }

}

