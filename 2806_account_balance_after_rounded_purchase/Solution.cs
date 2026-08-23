// LeetCode 2806 - Account Balance After Rounded Purchase
// https://leetcode.com/problems/account-balance-after-rounded-purchase/

public class Solution {
    public int AccountBalanceAfterPurchase(int purchaseAmount) {
        int r = ((purchaseAmount + 5) / 10) * 10;
        return 100 - r;
    }
}
