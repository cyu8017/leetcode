<?php
// LeetCode 0188 - Best Time to Buy and Sell Stock IV
// https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

class Solution {
    /**
     * @param Integer $k
     * @param Integer[] $prices
     * @return Integer
     */
    function maxProfit($k, $prices) {
        $n = count($prices);
        if ($n === 0 || $k === 0) {
            return 0;
        }
        if ($k >= intdiv($n, 2)) {
            $profit = 0;
            for ($index = 1; $index < $n; $index++) {
                $profit += max($prices[$index] - $prices[$index - 1], 0);
            }
            return $profit;
        }

        $buy = array_fill(0, $k + 1, PHP_INT_MAX);
        $sell = array_fill(0, $k + 1, 0);
        foreach ($prices as $price) {
            for ($transaction = 1; $transaction <= $k; $transaction++) {
                $buy[$transaction] = min($buy[$transaction], $price - $sell[$transaction - 1]);
                $sell[$transaction] = max($sell[$transaction], $price - $buy[$transaction]);
            }
        }

        return $sell[$k];
    }
}
