<?php
// LeetCode 2806 - Account Balance After Rounded Purchase
// https://leetcode.com/problems/account-balance-after-rounded-purchase/

class Solution {
    function accountBalanceAfterPurchase($purchaseAmount) {
        $r = intdiv($purchaseAmount + 5, 10) * 10;
        return 100 - $r;
    }
}
