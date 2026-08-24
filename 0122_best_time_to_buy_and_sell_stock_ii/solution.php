<?php
// LeetCode 0122 - Best Time to Buy and Sell Stock II
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution {
    /**
     * @param Integer[] $prices
     * @return Integer
     */
    function maxProfit($prices) {
        $profit = 0;
        for ($index = 1; $index < count($prices); $index++) {
            $profit += max(0, $prices[$index] - $prices[$index - 1]);
        }
        return $profit;
    }
}
