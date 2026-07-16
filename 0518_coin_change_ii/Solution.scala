// LeetCode 0518 - Coin Change II
// https://leetcode.com/problems/coin-change-ii/

object Solution {
  def change(amount: Int, coins: Array[Int]): Int = {
    val dp = Array.fill(amount + 1)(0)
    dp(0) = 1
    for (coin <- coins) {
      for (value <- coin to amount) {
        dp(value) += dp(value - coin)
      }
    }
    dp(amount)
  }
}
