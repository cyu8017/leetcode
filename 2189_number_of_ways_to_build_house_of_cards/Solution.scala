// LeetCode 2189 - Number of Ways to Build House of Cards
// https://leetcode.com/problems/number-of-ways-to-build-house-of-cards/

object Solution {
  def houseOfCards(n: Int): Int = {
    val dp = Array.fill(n + 1)(0)
    dp(0) = 1
    var k = 1
    while (3 * k - 1 <= n) {
      val cost = 3 * k - 1
      var j = n
      while (j >= cost) {
        dp(j) += dp(j - cost)
        j -= 1
      }
      k += 1
    }
    dp(n)
  }
}
