// LeetCode 2806 - Account Balance After Rounded Purchase
// https://leetcode.com/problems/account-balance-after-rounded-purchase/

class Solution {
    fun accountBalanceAfterPurchase(purchaseAmount: Int): Int {
        var r = ((purchaseAmount + 5) / 10) * 10
        return 100 - r
    }
}
