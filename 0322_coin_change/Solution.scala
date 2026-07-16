// LeetCode 0322 - Coin Change

// https://leetcode.com/problems/coin-change/



object Solution {

  def coinChange(coins: Array[Int], amount: Int): Int = {

    val maxValue = amount + 1

    val dp = Array.fill(amount + 1)(maxValue)

    dp(0) = 0

    for (coin <- coins) {

      for (value <- coin to amount) {

        dp(value) = math.min(dp(value), dp(value - coin) + 1)

      }

    }

    if (dp(amount) == maxValue) -1 else dp(amount)

  }

}

