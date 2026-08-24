<?php
// LeetCode 2412 - Minimum Money Required Before Transactions
// https://leetcode.com/problems/minimum-money-required-before-transactions/

class Solution {
    function minimumMoney($transactions) {
        $totalLoss = 0;
        $maxCashback = 0;
        $maxCost = 0;
        foreach ($transactions as $t) {
            $cost = $t[0];
            $cashback = $t[1];
            if ($cost > $cashback) {
                $totalLoss += $cost - $cashback;
                $maxCashback = max($maxCashback, $cashback);
            } else {
                $maxCost = max($maxCost, $cost);
            }
        }
        return max($totalLoss + $maxCashback, $totalLoss + $maxCost);
    }
}
