// LeetCode 1672 - Richest Customer Wealth
// https://leetcode.com/problems/richest-customer-wealth/

object Solution {
  def maximumWealth(accounts: Array[Array[Int]]): Int =
    accounts.map(_.sum).max
}
