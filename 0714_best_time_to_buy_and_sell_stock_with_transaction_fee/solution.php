<?php
// LeetCode 0714 - Best Time to Buy and Sell Stock with Transaction Fee
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

class Solution {
    function maxProfit($prices, $fee) {
        $hold = -$prices[0];
        $cash = 0;
        $n = count($prices);
        for ($i = 1; $i < $n; $i++) {
            $price = $prices[$i];
            $hold = max($hold, $cash - $price);
            $cash = max($cash, $hold + $price - $fee);
        }
        return $cash;
    }
}
