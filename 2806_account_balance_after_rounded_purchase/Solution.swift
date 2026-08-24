// LeetCode 2806 - Account Balance After Rounded Purchase
// https://leetcode.com/problems/account-balance-after-rounded-purchase/

class Solution {
    func accountBalanceAfterPurchase(_ purchaseAmount: Int) -> Int {
        100 - ((purchaseAmount + 5) / 10) * 10
    }
}
