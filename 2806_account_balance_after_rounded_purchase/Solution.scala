// LeetCode 2806 - Account Balance After Rounded Purchase
// https://leetcode.com/problems/account-balance-after-rounded-purchase/

object Solution {
  def accountBalanceAfterPurchase(purchaseAmount: Int): Int = {
    val r = ((purchaseAmount + 5) / 10) * 10
    100 - r
  }
}
