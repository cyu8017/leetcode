// LeetCode 1716 - Calculate Money in Leetcode Bank
// https://leetcode.com/problems/calculate-money-in-leetcode-bank/

object Solution {
  def totalMoney(n: Int): Int = {
    val weeks = n / 7
    val days = n % 7
    weeks * 28 + 7 * weeks * (weeks - 1) / 2 + days * (weeks + 1) + days * (days - 1) / 2
  }
}
