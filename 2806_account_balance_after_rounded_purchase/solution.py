# LeetCode 2806 - Account Balance After Rounded Purchase
# https://leetcode.com/problems/account-balance-after-rounded-purchase/


class Solution:
    def accountBalanceAfterPurchase(self, purchaseAmount: int) -> int:
        r = ((purchaseAmount + 5) // 10) * 10
        return 100 - r
